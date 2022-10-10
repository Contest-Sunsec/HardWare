import hardware #라즈베리파이 하드웨어 정보 값 불러오는 모듈
import time
import json
from pyfirmata import *

seri = serial.Serial(baudrate=9600,timeout=None, port = 'COM6') #시리얼 포트 설정
print("Serial name" + seri.name)#시리얼 포트 이름 출력

res = []

def get_sensor():   
    for i in range(0, 8):
        seri.write('g'.encode()) #시리얼 포트에 데이터 전송
        con = seri.readline() #시리얼 포트에서 데이터 수신
        con = con[:len(con)-1].decode().replace('\r', '')
        res.append(con)
    return res

def hardware_info():
    content = get_sensor()
    info =  {
        "id" : "A1B2C3", #FARMSELT Model Name
        "soilEc" : float(content[0]), #Soil EC Sensor Value
        "soilTemp" : float(content[1]),#Soil Temperature Sensor Value
        "soilHum" : float(content[2]), #Soil Humidity Sensor Value
        "airTemp" : float(content[3]), #Air Temperature Sensor Value
        "airHum" : float(content[4]), #Air Humidity Sensor Value
        "solar" : int(content[5]), #Sunlight Sensor Value
        "uptime":hardware.uptime_info,#hardware.uptime_info()
        "latitude": content[6], #Hardware GPS Sendsor Value 
        "longitude":content[7], #Hardware GPS Sendsor Value
        "speed":hardware.network_speed_test(),#hardware.network_speed_test()
        "ping": hardware.ping(),#hardware.ping_test()
        "bettery":hardware.hardware_voltage()#hardware.bettery_info()
    }
    return json.dumps(info)    

