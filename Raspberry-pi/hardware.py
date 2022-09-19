import os

def cpu_info():
    cpu_info = os.popen("grep ^'model name' /proc/cpuinfo").read()
    cpu_info = cpu_info.replace('model name', '').split(':')
    
    return cpu_info[1].replace('\n','')

def ram_info():
    MemTotal = os.popen("grep ^'MemTotal' /proc/meminfo").read()
    MemFree = os.popen("grep ^'MemFree' /proc/meminfo").read()

    MemTotal = MemTotal.replace("MemTotal:","").replace('kB','').replace(" ",'')
    MemTotal =  int(MemTotal) / float(1000000)

    MemFree = MemFree.replace("MemFree:","").replace('kB','').replace(' ','')
    MemFree = int(MemFree) / float(1000000)
    
    return "{}GB / {}GB".format(round(MemTotal,1), round(round(MemTotal,4) - round(MemFree,4), 2))
    
def os_info():
    os_info = os.popen("grep ^'PRETTY_NAME' /etc/os-release").read()
    
    return os_info.replace("PRETTY_NAME=","").replace('"',"").replace('\n','')
    
def kernel_info():
    kernel_info = os.popen("uname -r").read().replace('\n','')
    
    return kernel_info

def uptime_info():
    uptime_info = os.popen("uptime").read().replace('\n','')
    uptime_info = uptime_info.split(",")
    
    return uptime_info[0].replace("None","")

def network_info():
    network_info = os.popen("ip addr").read()
    network_info = network_info.split("inet")
    
    return network_info[3].split("/")[0].replace(" ","")

