
#MATHLIB="m" pip3 install numpy
import os
from moviepy.editor import *
from colorama import init,Fore,Back
init(autoreset=True)
YELLOW = "\x1b[1;33;40m" 
RED = "\x1b[1;31m"
GREEN="\x1b[1;32m"
def vdo():
    print(f"\n{YELLOW}Enter video fullname [$]: ", end='')
    vdopath = "/sdcard/Download/"+input()
    if vdopath == '/sdcard/Download/' :
       os.system("clear")
       os.system("bash gifbann")
       vdo()
    else:
       print(f"\n\t{RED}|<<<<<<<<<<<<<<<<<<Gif Duration>>>>>>>>>>>>>>>>>>|\n ", end='')
       print()
       print(f"\n{GREEN}<===Starting Time===>\n ", end='')
       startdur= input('Starting minute:  ')+","+ input('Starting second: ')
       print()
       print(f"\n{GREEN}<===Ending Time===>\n ", end='')
       enddur = input('Ending minute : ')+","+input('Ending second : ')
       print()
       print(Fore.RED + Back.GREEN + 'Please wait...')
       olaf = VideoFileClip(vdopath, audio=False)
       duration=olaf.subclip((startdur),(enddur))
       size=duration.resize(.95)
       speed=size.speedx(0.5)
       gifname= "/sdcard/Download/"+ input('Enter gifName to save: ')+".gif"
       if gifname == '/sdcard/Download/':
         os.system("clear")
         os.system("gifbann")
         vdo()
       else:
         speed.write_gif(gifname, fps=10, fuzz=2)
         print()
         print()
         print(f"\n\t  {YELLOW}Your Giffy save as "+str(gifname)+" Successfully! ")
         print()
vdo()
