print('''\
 _____ _          _____     _   ____       _
|_   _| |__   ___|  ___|_ _| |_|  _ \ __ _| |_
  | | | '_ \ / _ \ |_ / _` | __| |_) / _` | __|
  | | | | | |  __/  _| (_| | |_|  _ < (_| | |_
  |_| |_| |_|\___|_|  \__,_|\__|_| \_\__,_|\__| ''')

import os
import time
import random
import sys

print("\033[31m---!⚠️  -Warning you user Kali linux Run root!- ⚠️  !---\033[31m")
print("\033[0m")
print("[ 01 ]  install")
print("[ 02 ]  uninstall TheFatRat")
print("[ 03 ]  run TheFatRat")
print("[ 04 ]  exit")

op=int(input("Number tool: "))

if(op==1):
 os.system("git clone https://github.com/Screetsec/TheFatRat.git")
 os.system("cd TheFatRat")
 os.system("chmod +x setup.sh && ./setup.sh")
if(op==2):
 os.system("rm -r -f TheFatRat && clear && python3 TheFatRat.py")
if(op==3):
 os.system("cd TheFatRat")
 os.system("cd TheFatRat && chmod +x setup.sh && ./setup.sh")
if(op==4):
 os.system("clear")
 os.system("cd && cd Watch_dog-v0.1-file-linux && python3 DEDTHON-WATCH_DOG-FILE.py")