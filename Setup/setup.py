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

"""

# Move necessary files to this folder
source=pathlib.Path.cwd()/'FFMPEG'
shutil.move(source.__str__(),"C:\\youtube_dl\\FFMPEG")
user=os.getlogin()
print(user)