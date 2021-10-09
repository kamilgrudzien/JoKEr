import os
import sys
import ctypes
import time
import shutil
import socket
import subprocess
#using ctypes for wallpaper changes
#time we can use for delays and cycling changes

#GLOBAL VARIABLES
dir_path = "C:\WindowsLogs"
img = r"C:\Users\Kamil\Desktop\image.jpg"
img1 = r"C:\Users\Kamil\Desktop\v33r1.png"


#background is to set background of target machine
#need to update this to not include the absolute path
def background():
    #SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img, 0)

def ip_address():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    f = open("Ip_address.txt", "a")
    print("Your attacking Computer Name is:" + hostname, file=f)
    print("Your attacking Computer IP Address is:" + IPAddr, file=f)
    f.close()    

def copy_files(sourceFolder, targetFolder):
    shutil.copytree(sourceFolder, targetFolder)
    print("files copied")
    
def dir_create():
    #mode 0o777 allows for permissions to RWE
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path,mode = 0o777)
    else:
        print('The directory is present.')

def main():
    background()
    print("Wallpaper successfully applied")
    dir_create()
    print("Directory successfully created")

if __name__ == "__main__":
    main ()
