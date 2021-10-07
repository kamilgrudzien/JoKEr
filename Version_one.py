import os, shutil
import socket
import sys
#import struct
#import ctypes



def main():
    #Get IP adddress and Host Name
    ip_address()


    #make target files, source files
    os.chdir('.')
    target_folder = r'C:\Users\Jenny McCyber\Documents\JoKEr_Virus\new.txt'
    source_folder = r'C:\Users\Jenny McCyber\Documents\Test' + '\\'
    
    copy_files(source_folder, target_folder)

    #Run server
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
    
        
def copy_files(sourceFolder, targetFolder):

    shutil.copytree(sourceFolder, targetFolder)
    print("files copied")

    


    
if __name__ == "__main__":
    main()
