#!/usr/bin/env python

import subprocess 
import os
import shutil
import pathlib
import winreg
success=0

########## Installer youtube-dl ##########
yt_dl = subprocess.run('pip install youtube-dl --upgrade',shell=True,capture_output=True,text=True)
if yt_dl.returncode==0:
    print("1. SUCCESS : " + yt_dl.stdout)
    success+=1
else:
    print("1. ERROR : " + yt_dl.stderr)



########## Installer FFMPEG ##########
# Define a directory to install FFMPEG
path1 = "C:/youtube_dl"

try:
    os.mkdir(path1)
except OSError:
    print ("2. ERROR : Creation of the directory %s failed" % path1)
else:
    print ("2. SUCCESS : Successfully created the directory %s " % path1)
    success+=1




# Move necessary files to this folder
source=pathlib.Path(__file__).parent.absolute()/'FFMPEG'

try:
    shutil.move(source.__str__(),"C:\\youtube_dl")
except OSError as err:
    print("3. ERROR :" + err)
else:
    print("3. SUCCESS : FFMPEG was successfully installed to C:/youtube_dl/FFMPEG")
    success+=1





########## Add default config to youtube-dl ##########

# Create youtube-dl folder in Roaming
dir_path = os.path.join(os.environ['APPDATA'],'youtube-dl')
try:
    os.mkdir(dir_path)
except OSError as err2:
    print ("4.1 ERROR : Creation of the directory %s failed" % dir_path)
    print("4.1 ERROR : "+ err2)
else:
    print ("4.1 SUCCESS : Successfully created the directory %s " % dir_path)
    success+=1

# Create "config.txt"
filepath=os.path.join(dir_path,"config.txt")
f = open(filepath,"w")

Lines=["# Lines starting with # are comments \n","\n",
"# Always extract audio \n",
"-f bestaudio[ext=m4a] \n",
"#-f 'bestvideo[ext=mp4]+bestaudio[ext=m4a] \n","\n",
"# Do not copy the mtime \n",
"--no-mtime \n","\n",
"# Save in Download directory \n",
"-o ~/Downloads/%(title)s.%(ext)s \n","\n",
"--ffmpeg-location C:/youtube_dl/FFMPEG/bin \n","\n",
"# convert to mp3 \n",
"# --extract-audio --audio-format mp3]"]

f.writelines(Lines)
f.close()

if os.path.isfile(filepath):
    print("4.2 SUCCESS : config file was created")
    success+=1
else:
    print("4.2. ERROR : config file is missing")


########## Install command runner App ##########

#Move App folder to youtube-dl folder
sourceApp=pathlib.Path(__file__).resolve().parent.parent/'app'

try:
    shutil.move(sourceApp.__str__(),"C:\\youtube_dl")
except OSError as err:
    print("5.1 ERROR :")
    print(err)
else:
    print("5.1 SUCCESS : App was successfully installed to C:/youtube_dl/app")
    success+=1


# Add Native Messaging Registry Keys
# CURRENT_USER
try:
    winreg.CreateKey(winreg.HKEY_CURRENT_USER,"Software\\Mozilla\\NativeMessagingHosts\\firefox_command_runner")
    a_Key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,"Software\\Mozilla\\NativeMessagingHosts\\firefox_command_runner", 0, winreg.KEY_WRITE)
    winreg.SetValueEx(a_Key,"",0,winreg.REG_SZ,"C:\\youtube_dl\\app\\firefox_command_runner.json")
    winreg.CloseKey(a_Key)
except OSError as err:
    print("5.2 ERROR :")
    print(err)
else:
    print("5.2 SUCCESS : Registry Key was created")
    success+=1

########## Print if the installation went well ##########
if success==7:
    print("\nThe installation is successful")
else:
    print("\nSomething went wrong. Please check errors messages")

