import os

def cpu_info():
    #CPU Model info
    cpu_info = os.popen("grep ^'model name' /proc/cpuinfo").read()
    cpu_info = cpu_info.replace('model name', '').split(':')
    return cpu_info[1].replace('\n','')

def ram_info():
    #Total Memory / Used Memory
    MemTotal = os.popen("grep ^'MemTotal' /proc/meminfo").read()
    MemFree = os.popen("grep ^'MemFree' /proc/meminfo").read()

    MemTotal = MemTotal.replace("MemTotal:","").replace('kB','').replace(" ",'')
    MemTotal =  int(MemTotal) / float(1000000)

    MemFree = MemFree.replace("MemFree:","").replace('kB','').replace(' ','')
    MemFree = int(MemFree) / float(1000000)
    
    return "Total Memory : {}GB / Used Memory {}GB".format(round(MemTotal,1), round(round(MemTotal,4) - round(MemFree,4), 2))
    
def os_info():
    #OS info
    os_info = os.popen("grep ^'PRETTY_NAME' /etc/os-release").read()
    return os_info.replace("PRETTY_NAME=","").replace('"',"").replace('\n','')
    
def kernel_info():
    #Kernel info
    kernel_info = os.popen("uname -r").read().replace('\n','')
    return kernel_info

def uptime_info():
    #Uptime info
    uptime_info = os.popen("uptime").read().replace('\n','')
    uptime_info = uptime_info.split(",")
    return uptime_info[0].replace("None","")

def network_info():
    #Local Network IP info
    network_info = os.popen("ip addr").read()
    network_info = network_info.split("inet")
    return network_info[3].split("/")[0].replace(" ","")

def time_info():
    #Time info
    time_info = os.popen("date").read()
    return time_info.replace('\n','')

def network_speed_test():
    #Network Speed Test
    network_speed_test = os.popen("speedtest-cli --secure").read()
    network_speed = network_speed_test.split("\n")
    
    return "Download Speed: {}  Upload Speed: {}".format(network_speed[6].replace("Download: ",""), network_speed[8].replace("Upload: ",""))

def ping(address):
    #ping address
    ping = os.popen("ping -c 1 {}".format(address)).read()
    return ping

def hardware_voltage():
    #Hardware Voltage
    hardware_voltage = os.popen("vcgencmd measure_volts").read()
    return hardware_voltage.replace("volt=","").replace("\n","")

def apt_update():
    os.system("sudo apt update")
    os.system("sudo apt upgrade -y")

def apt_install():
    os.system("apt install -y python3-pip")
    os.system("apt install -y Arduino")
    os.system("apt install -y speedtest-cli")
    