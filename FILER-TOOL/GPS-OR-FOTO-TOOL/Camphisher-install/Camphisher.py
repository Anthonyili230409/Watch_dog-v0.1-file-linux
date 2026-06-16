print('''\
██ ███    ██ ███████ ████████  █████  ██      ██                              
██ ████   ██ ██         ██    ██   ██ ██      ██                              
██ ██ ██  ██ ███████    ██    ███████ ██      ██                              
██ ██  ██ ██      ██    ██    ██   ██ ██      ██                              
██ ██   ████ ███████    ██    ██   ██ ███████ ███████                         
                                                                              
                                                                              
 ██████  █████  ███    ███ ██████  ██   ██ ██ ███████ ██   ██ ███████ ██████  
██      ██   ██ ████  ████ ██   ██ ██   ██ ██ ██      ██   ██ ██      ██   ██ 
██      ███████ ██ ████ ██ ██████  ███████ ██ ███████ ███████ █████   ██████  
██      ██   ██ ██  ██  ██ ██      ██   ██ ██      ██ ██   ██ ██      ██   ██ 
 ██████ ██   ██ ██      ██ ██      ██   ██ ██ ███████ ██   ██ ███████ ██   ██ ''')

import os
import time
import random
import sys

print("[ 01 ]  install")
print("[ 02 ]  uninstall Camphisher")
print("[ 03 ]  run Camphisher")
print("[ 04 ]  exit")

op=int(input("Number tool: "))

if(op==1):
 os.system("git clone https://github.com/Anthonyili230409/Camphish")
 os.system("cd Camphish")
 os.system("cd Camphish && bash camphish.sh")
if(op==2):
 os.system("rm -r Camphish && clear && python3 Camphisher.py")
if(op==3):
 os.system("cd Camphish")
 os.system("cd Camphish && bash camphish.sh")
if(op==4):
 os.system("clear")
 os.system("cd && cd Watch_dog-v0.1-file-linux && python3 DEDTHON-WATCH_DOG-FILE.py")