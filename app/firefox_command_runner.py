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
# given its content.
def encodeMessage(messageContent):
    encodedContent = json.dumps(messageContent).encode('utf-8')
    encodedLength = struct.pack('@I', len(encodedContent))
    return {'length': encodedLength, 'content': encodedContent}

# Send an encoded message to stdout
def sendMessage(encodedMessage):
    sys.stdout.buffer.write(encodedMessage['length'])
    sys.stdout.buffer.write(encodedMessage['content'])
    sys.stdout.buffer.flush()

# Execute a commandline program with printed output
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
    # receivedMessage is audio_format+url concatenated
    receivedMessage = getMessage()
    audio_format=receivedMessage[0:3]
    url=receivedMessage[3:]
    Lines=[]
    
    # Adjust audio format cmd
    if(audio_format=='m4a'):
        cmd = ["youtube-dl","-f","bestaudio[ext=m4a]","--ffmpeg-location","C:/youtube_dl/FFMPEG/bin","--no-mtime","-w",url] 
    elif(audio_format=='mp3'):
        cmd = ["youtube-dl","-f","bestaudio[ext=m4a]","--ffmpeg-location","C:/youtube_dl/FFMPEG/bin","--no-mtime","-w","--extract-audio","--audio-format","mp3",url]
    else:
        cmd = ["youtube-dl","-f","bestvideo[ext=mp4]+bestaudio[ext=m4a]","--ffmpeg-location","C:/youtube_dl/FFMPEG/bin","--no-mtime","-w",url]
    logging.warning(cmd)

    # exec yt_dl program
    for x in execute(cmd):
        x=x.strip()
        Lines.append(x)
        part=Lines[-1].split()
        sendMessage(encodeMessage(["PROG",part]))


    # Progression information

    # Gather logs send a notification when download ends
    End_Notif=[] 
    for x in Lines:
        if(x.startswith('[download] 100%')):
            mes2="Download : "+x.strip()[11:]
            logging.warning(mes2)
            End_Notif.append(mes2.strip())
        elif(x.startswith('[download] Destination:') and audio_format != "mp4"):
            mes1=x[11:-3]+audio_format
            logging.warning(mes1)
            End_Notif.append(mes1.strip())
        elif(x.startswith('[ffmpeg] Merging formats')):
            mes="Destination: " + x[31:-1]
            logging.warning(mes)
            End_Notif.append(mes.strip())
    logging.warning(End_Notif)
    fullNotif=""
    for i in range(len(End_Notif)-1):
        fullNotif += End_Notif[i]
        fullNotif += "\n" 
    fullNotif += End_Notif[-1]
    sendMessage(encodeMessage(["END",fullNotif]))

