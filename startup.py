import os

def apt_update():
    os.system("sudo apt update")
    os.system("sudo apt upgrade -y")

def apt_install():
    os.system("apt install -y python3-pip")
    os.system("apt install -y Arduino")
    os.system("apt install -y speedtest-cli")
    