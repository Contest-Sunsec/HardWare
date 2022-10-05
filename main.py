from urllib import request
import hardware
import json_data
import time
import requests

hardware.apt_update()
hardware.apt_install()

url = open("config.txt").read()
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

while(1):
    requests.post(url, data=json_data.hardware_info(), headers=headers)
    requests.post(url, data=json_data.sensor_info(), headers=headers)
    time.sleep(900)
    