import hardware #라즈베리파이 하드웨어 정보 값 불러오는 모듈
import time
import json
from pyfirmata import *

board = Arduino('/dev/ttyACM0') #시리얼 포트 지정
seri = serial.Serail(board, baudrate=9600,timeout=None) #시리얼 포트 설정
print("Serial name" + seri.name)#시리얼 포트 이름 출력

def get_sensor():   
    seri.write('g'.encode()) #시리얼 포트에 데이터 전송
    content = seri.readline() #시리얼 포트에서 데이터 수신
    return content


def hardware_info():
    content = get_sensor()
    content.split(' ')
    info =  {
        "id" : "FARMSELT-example-1234", #FARMSELT Model Name
        "soilEc" : float(content[0]), #Soil EC Sensor Value
        "soilTemp" : float(content[2]),#Soil Temperature Sensor Value
        "soilHum" : float(content[4]), #Soil Humidity Sensor Value
        "airTemp" : float(content[6]), #Air Temperature Sensor Value
        "airHum" : float(content[8]), #Air Humidity Sensor Value
        "solar" : int(content[10]), #Sunlight Sensor Value
        "uptime":hardware.uptime_info,#hardware.uptime_info()
        "speed":hardware.network_speed_test(),#hardware.network_speed_test()
        "ping": hardware.ping(),#hardware.ping_test()
        "latitude": content[12], #Hardware GPS Sendsor Value 
        "longitude":content[14], #Hardware GPS Sendsor Value

    }
    return json.dumps(info)    

