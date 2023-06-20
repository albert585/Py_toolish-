import os
import wget
def detect():
    if os.path.exists("/usr/bin/pacman"):
        print("检测到您的系统为ArchLinux或其他Arch系系统")
        wget.download("https://www.linuxfromscratch.org/blfs/downloads/stable/BLFS-BOOK-11.3-nochunks.html")
detect()