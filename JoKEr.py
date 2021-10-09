import os
import sys
import ctypes
import time
#using ctypes for wallpaper changes
#time we can use for delays and cycling changes

#GLOBAL VARIABLES
img = r"C:\Users\Kamil\Desktop\image.jpg"
img1 = r"C:\Users\Kamil\Desktop\v33r1.png"


#background is to set background of target machine
#need to update this to not include the absolute path
def background():
    #SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img1, 0)
    

def main():
    background()
    print("Wallpaper successfully applied")

if __name__ == "__main__":
    main ()
