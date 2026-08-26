print('''\
██     ██  █████  ████████  ██████ ██   ██         ██████   ██████   ██████  
██     ██ ██   ██    ██    ██      ██   ██         ██   ██ ██    ██ ██       
██  █  ██ ███████    ██    ██      ███████         ██   ██ ██    ██ ██   ███ 
██ ███ ██ ██   ██    ██    ██      ██   ██         ██   ██ ██    ██ ██    ██ 
 ███ ███  ██   ██    ██     ██████ ██   ██ ███████ ██████   ██████   ██████  
                                                                             
                                                                             
██    ██  ██████      ██                                                     
██    ██ ██  ████    ███                                                     
██    ██ ██ ██ ██     ██                                                     
 ██  ██  ████  ██     ██                                                     
  ████    ██████  ██  ██                                                     
                                                                             
                                                                             
███████ ██ ██      ███████                                                   
██      ██ ██      ██                                                        
█████   ██ ██      █████                                                     
██      ██ ██      ██                                                        
██      ██ ███████ ███████   ''')


import os
import time
import random
import sys
print("--------------- Welcome DEDTHON Linux github tool!------------------")

print("[ 01 ]  GPS OR FOTO or tool")
print("[ 02 ]  TheFatRat")

# command real "input" text you keybord 1
op=int(input("Number tool: "))

# command run intall or github
if(op==1):
 os.system("clear")
 os.system("cd FILER-TOOL && cd GPS-OR-FOTO-TOOL && python3 GPS-OR-FOTO.py")
if(op==2):
  os.system("clear")
  os.system("cd FILER-TOOL && cd TheFatRat && python3 TheFatRat.py")