#!/usr/bin/env python

import sys
import os
import json
import struct
import subprocess
import tempfile
import logging
logging.basicConfig(filename='app.log',filemode='w',format='%(name)s - %(levelname)s - %(message)s')

# Read a message from stdin and decode it.
def getMessage():
    rawLength = sys.stdin.buffer.read(4)
    if len(rawLength) == 0:
        sys.exit(0)
    messageLength = struct.unpack('@I', rawLength)[0]
    message = sys.stdin.buffer.read(messageLength).decode('utf-8')
    return json.loads(message)

# Encode a message for transmission,
def encodeMessage(messageContent):
    encodedContent = json.dumps(messageContent).encode('utf-8')
    encodedLength = struct.pack('@I', len(encodedContent))
    return {'length': encodedLength, 'content': encodedContent}

# Send an encoded message to stdout
def sendMessage(encodedMessage):
    sys.stdout.buffer.write(encodedMessage['length'])
    sys.stdout.buffer.write(encodedMessage['content'])
    sys.stdout.buffer.flush()

# Execute a commandline program with capturable realtime output
def execute(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line 
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        error_code=subprocess.CalledProcessError(return_code, cmd)
        res="The file couldn't be downloaded with error code : " + error_code
        sendMessage(encodeMessage(res))
        logging.warning(res)
        raise error_code
        

while True:
    # Capture incoming message
    receivedMessage = getMessage()

    if(receivedMessage=="OpenDL"):
        DL_Folder=os.path.expanduser("~")+"\\Downloads"    
        subprocess.call('explorer '+ DL_Folder) 

    elif(receivedMessage[0:6]=="format"):
        url = receivedMessage[6:]

        # Ask for available format and store output to a list
        cmd = ["youtube-dl","-F",url]
        available_formats = subprocess.run(cmd,shell=True,capture_output=True,text=True)
        Lines = available_formats.stdout.splitlines()
        Lines = Lines[3:-1]

        # Format cmd output to list of [video_code,'mp4','720p','40.05MiB']
        L_proc=[]
        logging.warning(Lines)
        for i in range(len(Lines)):
            L = Lines[i].split(" ")
            L = [word for word in L if(word!="" and word !=',' and word !='(best)')]
            logging.warning(L)
            if(L[1]=='mp4'):
                L = L[0:2]+L[3:4]+L[-1:]
                L_proc.append(L)
        
        # Find duplicate formats and select the best version 
        L_proc = sorted(L_proc, key=lambda x: int(x[2][:-1]))
        logging.warning(L_proc)   
        id_to_del=[]
        for i in range(len(L_proc)-1):
            if(L_proc[i][2]==L_proc[i+1][2]):
                print(float(L_proc[i][3][:-3])<float(L_proc[i+1][3][:-3]))
                if(float(L_proc[i][3][:-3])<float(L_proc[i+1][3][:-3])):
                    id_to_del.append(i)
                else:
                    id_to_del.append(i+1)

        # Delete duplicate with lowest quality
        for x in id_to_del:
            del L_proc[x-id_to_del.index(x)]
        logging.warning(id_to_del)
        logging.warning(L_proc)
        sendMessage(encodeMessage(["FORMAT",L_proc]))

    # audio_format or video_code for download
    else :
        audio_format=receivedMessage[0:3]
        url = receivedMessage[3:]
        Lines = []
        
        # Adjust audio format cmd
        if(audio_format=='m4a'):
            cmd = ["youtube-dl","-f","bestaudio[ext=m4a]","--ffmpeg-location","C:/youtube_dl/FFMPEG/bin","--no-mtime","-w",url] 
        elif(audio_format=='mp3'):
            cmd = ["youtube-dl","-f","bestaudio[ext=m4a]","--ffmpeg-location","C:/youtube_dl/FFMPEG/bin","--no-mtime","-w","--extract-audio","--audio-format","mp3",url]
        elif(audio_format=='mp4'):
            cmd = ["youtube-dl","-f","bestvideo[ext=mp4]+bestaudio[ext=m4a]","--ffmpeg-location","C:/youtube_dl/FFMPEG/bin","--no-mtime","-w",url]
        else: # custom video format
            cmd = ["youtube-dl","-f",audio_format+"+bestaudio[ext=m4a]","--ffmpeg-location","C:/youtube_dl/FFMPEG/bin","--no-mtime","-w",url]

        # exec yt_dl program and send progress data
        for x in execute(cmd):
            x = x.strip()
            Lines.append(x)
            part = Lines[-1].split()
            sendMessage(encodeMessage(["PROG",part]))

        # Send Process logs & Send a ending notification
        End_Notif=[] 
        logging.critical(Lines)
        for x in Lines:
            if(x.startswith('[download] 100%')):
                mes2 = "Download : "+x.strip()[11:]
                logging.warning(mes2)
                End_Notif.append(mes2.strip())
            elif(x.startswith('[download] Destination:') and audio_format != "mp4"):
                mes1 = x[11:-3]+audio_format
                logging.warning(mes1)
                End_Notif.append(mes1.strip())
            elif(x.startswith('[ffmpeg] Merging formats')):
                mes = "Destination: " + x[31:-1]
                logging.warning(mes)
                End_Notif.append(mes.strip())
            elif(x.endswith("downloaded and merged") or x.endswith("has already been downloaded")):
                mes = x[11:]
                logging.warning(mes)
                End_Notif.append(mes.strip())

        logging.warning(End_Notif)
        fullNotif=""
        for i in range(len(End_Notif)-1):
            fullNotif += End_Notif[i]
            fullNotif += "\n" 
        fullNotif += End_Notif[-1]
        sendMessage(encodeMessage(["END",fullNotif]))