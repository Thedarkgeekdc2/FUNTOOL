
#MATHLIB="m" pip3 install numpy

banner="""banner() {
    clear
    echo -e "\e[1;31m"
    if ! [ -x "$(command -v figlet)" ]; then
        echo 'Introducing GIFFYTOOL'
    else                                                                                                figlet GIF-Tool
    fi
    if ! [ -x "$(command -v toilet)" ]; then
        echo -e "\e[4;34m This TOOL Was Created By \e[1;32mHUNT3R \e[0m"
    else
        echo -e "\e[1;34mCreated By \e[1;34m"
        toilet -f mono12 -F border HUNT3R
    fi
    echo -e "\e[1;32m           Managed By: DINESH CHAUDHARY \e[0m"
    echo " "
    echo " "                                                                                        echo -e "\e[1;33m Warning:  \e[0m"
    echo -e "\e[1;31m ENTER YOUR VIDEO NAME with .mp4 Located only /Storage/Download  \e[0m"
    echo -e "\e[1;31m This tool only Suppurted .mp4 files. [Entry Corret = No ERROR!] \e[0m"
}
banner
"""
myFile = open("bnna", "w")
myFile.write(banner)
myFile.close()


import os
from moviepy.editor import *
from colorama import init,Fore,Back
init(autoreset=True)
os.system("bash bnna")

YELLOW = "\x1b[1;33;40m" 
RED = "\x1b[1;31m"
GREEN="\x1b[1;32m"
def vdo():
    print(f"\n{YELLOW}Enter video fullname [$]: ", end='')
    vdopath = "/sdcard/Download/"+input()
    if vdopath == '/sdcard/Download/' :
       os.system("clear")
       os.system("bash bnna")
       vdo()
       os.system("rm bnna")
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
         os.system("bnna")
         vdo()
         os.system("bnna")
       else:
         speed.write_gif(gifname, fps=10, fuzz=2)
         print()
         print()
         print(f"\n\t  {YELLOW}Your Giffy save as "+str(gifname)+" Successfully! ")
         print()
vdo()
