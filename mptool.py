
import os
import random
from colorama import Fore,Style,init
from tqdm import tqdm
from time import sleep
import sys
from gtts import gTTS

def bann_text():
    os.system("clear")
    logo = """
     ╔════════════════════════════════════════════════════════════════════════════════════╗
     ║                                                                                    ║
     ║  ███╗   ███╗██████╗ ██████╗     ██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗   ║
     ║  ████╗ ████║██╔══██╗╚════██╗    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗  ║
     ║  ██╔████╔██║██████╔╝ █████╔╝    ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝  ║
     ║  ██║╚██╔╝██║██╔═══╝  ╚═══██╗    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗  ║
     ║  ██║ ╚═╝ ██║██║     ██████╔╝    ██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║  ║
     ║  ╚═╝     ╚═╝╚═╝     ╚═════╝     ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝  ║
     ╚════════════════════════════════════════════════════════════════════════════════════╝
                                         """
    if ASCII_MODE:
        logo = ""
    author = "Created By: "+"𝗗𝗜𝗡𝗘𝗦𝗛 𝗖𝗛𝗔𝗨𝗗𝗛𝗔𝗥𝗬"
    hint =  "𝐇𝐢𝐧𝐭 := " + "𝖲𝖾𝗅𝖾𝖼𝗍 & 𝖲𝖺𝗏𝖾 𝖿𝗂𝗅𝖾𝗌 𝗈𝗇𝗅𝗒 𝖥𝗋𝗈𝗆 /𝗦𝘁𝗼𝗿𝗮𝗴𝗲/𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱/"
    print(random.choice(ALL_COLORS)+ author + RESET_ALL)
    print(random.choice(ALL_COLORS) + logo + RESET_ALL)
    print()
    print(random.choice(ALL_COLORS) + hint)
    print()
    print()


ALL_COLORS = [Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.BLUE,
              Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
RESET_ALL = Style.RESET_ALL
ASCII_MODE = False
init(autoreset=True)
YELLOW = "\x1b[1;33;40m"
RED = "\x1b[1;31m"



def progress():
  for i in tqdm(range(0,5),colour="#ff1dce", desc="Loading Tool: "):
     sleep(0.1)


def player():
    print(f"\n{YELLOW}Enter txt filename [$]: ",end='')
    textpath= "/sdcard/Download/"+input()
    if textpath=='/sdcard/Download/':
      os.system("clear")
      bann_text()
      player()
    else:
      lines = open(textpath).read()
      language = 'en'
      myobj = gTTS(text=lines, lang= language, slow=False)
      print(f"\n{YELLOW}Enter mp3 filename to save [$]: ",end='')
      txtfsv = "/sdcard/Download/"+input()+ ".mp3"
      myobj.save(txtfsv)
      print(f"\t\n{RED}MP3 save as "+str(txtfsv)+" Succesfully!\n  ",end='')

def dirct():
    print(f"\n{YELLOW}Enter text to convert mp3 [$]: ",end='')
    txtt= input()
    if txtt=='':
       os.system("clear")
       bann_text()
       dirct()
    else:
      #lines = open(txtt).read()
      language = 'en'
      myobj = gTTS(text=txtt, lang= language, slow=False)
      print(f"\n{YELLOW}Enter mp3 filename to save [$]: ",end='')
      txtsv = "/sdcard/Download/"+input()+ ".mp3"
      myobj.save(txtsv)
      print(f"\t\n{RED}MP3 save as "+str(txtsv)+" Succesfully!\n",end='')

def play():
     print(f"\n{YELLOW}Enter MP3 name to Play [$]: ",end='')
     os.system("read ggg && mplayer /sdcard/Download/$ggg")




def selectnode(mode):
    mode = mode.lower().strip()
    try:
       bann_text()
       if mode == "convert textfile":
          player()
       elif mode == "convert ur typing" :
          dirct()
       else:
          raise KeyboardInterrupt
    except KeyboardInterrupt:
       play()
       print()
       sys.exit()






choice = ""
avail_choice = {
            "1": "Convert TextFile",
            "2": "Convert ur typing",
            "3": "Play Song"
}
try:
    while (choice not in avail_choice):
          bann_text()
          progress()
          os.system("clear")
          bann_text()
          print(random.choice(ALL_COLORS) + "Available Options:\n")
          for key, value in avail_choice.items():
             print("[ {key} ] {value} TO MP3".format(key=key,
                                        value=value))
          print()
          choice = input("Enter Choice : ")
    selectnode(mode=avail_choice[choice].lower())
except KeyboardInterrupt:
      print("Received INTR call - Exiting...")
      sys.exit()
