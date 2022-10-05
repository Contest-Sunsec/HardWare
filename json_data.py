import hardware #라즈베리파이 하드웨어 정보 값 불러오는 모듈
import time
import json
from pyfirmata import *

board = Arduino('/dev/ttyACM0') #시리얼 포트 지정
seri = serial.Serail(board, baudrate=9600,timeout=None) #시리얼 포트 설정
print("Serial name" + seri.name)#시리얼 포트 이름 출력

def get_sensor():
    seri.write('1'.encode()) #시리얼 포트에 데이터 전송
    content = seri.readline() #시리얼 포트에서 데이터 수신
    return content

def get_info():
    seri.write('2'.encode()) #시리얼 포트에 데이터 전송
    content = seri.readline() #시리얼 포트에서 데이터 수신
    return content

def hardware_info():
    info =  {
        "time":time.time(),
        "uptime":"hi",#hardware.uptime_info(),
        "latitude":"dfedf", #Hardware GPS Sendsor Value 
        "longitude":"dfedf", #Hardware GPS Sendsor Value
        "internet":hardware.network_speed_test(),#hardware.network_speed_test()
    }
    
    return json.dumps(info)

def return_data():
    content = get_sensor()
    info = {
        "soil_ec" : content[0], #Soil EC Sensor Value
        "soil_temp" : content[2],#Soil Temperature Sensor Value
        "soil_humidity" : content[4], #Soil Humidity Sensor Value
        "air_temp" : content[6], #Air Temperature Sensor Value
        "air_humidity" : content[8], #Air Humidity Sensor Value
        "sunlight" : content[10], #Sunlight Sensor Value
    }
    return json.dumps(info)    

