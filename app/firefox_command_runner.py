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

while True:
    # receivedMessage is audio_format+url concatenated
    receivedMessage = getMessage()
    audio_format=receivedMessage[0:3]
    url=receivedMessage[3:]

    # exec yt_dl program
    if(audio_format=='m4a'):
        yt_dl = subprocess.run('youtube-dl -f bestaudio[ext=m4a] --no-mtime -w -o ~/Downloads/%(title)s.%(ext)s '+url,shell=True,capture_output=True,text=True)
    elif(audio_format=='mp3'):
        yt_dl = subprocess.run('youtube-dl -f bestaudio[ext=m4a] --no-mtime -w -o ~/Downloads/%(title)s.%(ext)s --extract-audio --audio-format "mp3" '+url,shell=True,capture_output=True,text=True)
    else:
        yt_dl = subprocess.run('youtube-dl -f bestvideo[ext=mp4]+bestaudio[ext=m4a] --no-mtime -w -o ~/Downloads/%(title)s.%(ext)s '+url,shell=True,capture_output=True,text=True)
    
    logging.warning(yt_dl.stdout)

    # Gather logs send a notification when download ends
    if yt_dl.returncode==0:
        Lines=yt_dl.stdout.splitlines() #yt_dl logs
        Notif=[] 
        for x in Lines:
            if(x.startswith('[download] 100%')):
                mes2="Download : "+x.strip()[11:]
                logging.warning(mes2)
                Notif.append(mes2.strip())
            elif(x.startswith('[download] Destination:') and audio_format != "mp4"):
                mes1=x[11:-3]+audio_format
                logging.warning(mes1)
                Notif.append(mes1.strip())
            elif(x.startswith('[ffmpeg] Merging formats')):
                mes="Destination: " + x[31:-1]
                logging.warning(mes)
                Notif.append(mes.strip())
        logging.warning(Notif)
        fullNotif=""
        for i in range(len(Notif)-1):
            fullNotif += Notif[i]
            fullNotif += "\n" 
        fullNotif += Notif[-1]
        sendMessage(encodeMessage(fullNotif))
    else :
        error_code=yt_dl.stderr
        res="The file couldn't be downloaded with error code : " + error_code
        sendMessage(encodeMessage(res))
        logging.warning(res)

