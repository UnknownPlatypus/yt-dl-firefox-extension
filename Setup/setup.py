#!/usr/bin/env python

import subprocess 
import os
import shutil
import pathlib

"""
########## Installer youtube-dl ##########
yt_dl = subprocess.run('pip install youtube-dl --upgrade',shell=True,capture_output=True,text=True)
# print(yt_dl.stdout)



########## Installer FFMPEG ##########
# Define a directory to install FFMPEG
path1 = "C:/youtube_dl"
path2 = "C:/youtube_dl/FFMPEG"

try:
    os.mkdir(path1)
except OSError:
    print ("Creation of the directory %s failed" % path1)
else:
    print ("Successfully created the directory %s " % path1)

try:
    os.mkdir(path2)
except OSError:
    print ("Creation of the directory %s failed" % path2)
else:
    print ("Successfully created the directory %s " % path2)


# Move necessary files to this folder
source=pathlib.Path(__file__).parent.absolute()/'FFMPEG'
shutil.move(source.__str__(),"C:\\youtube_dl")

########## Add default config to youtube-dl ##########

# Create youtube-dl folder in Roaming
dir_path = os.path.join(os.environ['APPDATA'],'youtube-dl')
try:
    os.mkdir(dir_path)
except OSError:
    print ("Creation of the directory %s failed" % dir_path)
else:
    print ("Successfully created the directory %s " % dir_path)

# Create "config.txt"
filepath=os.path.join(dir_path,"config.txt")
f = open(filepath,"w")

Lines=["# Lines starting with # are comments \n","\n",
"# Always extract audio \n",
"-f bestaudio[ext=m4a] \n",
"#-f 'bestvideo[ext=mp4]+bestaudio[ext=m4a] \n","\n",
"# Do not copy the mtime \n"
,"--no-mtime \n","\n",
"# Save all videos under Movies directory in your home directory \n",
"-o C:/Users/<username>/Downloads/%(title)s.%(ext)s",
"# convert to mp3 \n","\n","# --extract-audio --audio-format mp3]"]

f.writelines(Lines)
f.close()


########## Install command runner App ##########

#Move Files to youtube-dl folder
sourceApp=pathlib.Path(__file__).parent.parent.absolute()/'app'
shutil.move(sourceApp.__str__(),"C:\\youtube_dl")
"""
# Add Native Messaging Registry Keys
