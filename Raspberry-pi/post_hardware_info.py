import json
import time
import os 
import requests
import hardware

hardware_url = "https://api.plebea.site/hardware"

def post_hardware_info():

    info = {
        'cpu': hardware.cpu_info(),
        'ram': hardware.ram_info(),
        'os': hardware.os_info(),
        'kernel': hardware.kernel_info(),
        'uptime': hardware.uptime_info()
    }
    
    json_data =json.dumps(info, indent=2)
    
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    requests.post(hardware_url, data=json_data, headers=headers)
    
while(1): #5 min loop
    post_hardware_info()
    print("post")
    time.sleep(300)
