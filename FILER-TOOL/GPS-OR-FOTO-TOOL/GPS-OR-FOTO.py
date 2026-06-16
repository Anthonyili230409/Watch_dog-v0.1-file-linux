print('''\
 ██████  ██████  ███████      ██████  ██████      ███████  ██████  ████████  ██████  
██       ██   ██ ██          ██    ██ ██   ██     ██      ██    ██    ██    ██    ██ 
██   ███ ██████  ███████     ██    ██ ██████      █████   ██    ██    ██    ██    ██ 
██    ██ ██           ██     ██    ██ ██   ██     ██      ██    ██    ██    ██    ██ 
 ██████  ██      ███████      ██████  ██   ██     ██       ██████     ██     ██████  ''')

import os
import time
import random
import sys

print("--------------- GPS OR FOTO TOOL  ------------------")

print("[ 01 ]  install - CAMPHISHER")
print("[ 02 ]  exit")

op=int(input("Number tool: "))

if(op==1):
 os.system("clear")
 os.system("cd Camphisher-install && python3 Camphisher.py") 
if(op==2):
 os.system("clear")
 os.system("cd && cd Watch_dog-v0.1-file-linux && python3 DEDTHON-WATCH_DOG-FILE.py")