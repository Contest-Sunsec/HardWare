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
        "longitude":"dfedf",
        "internet":hardware.network_speed_test(),#hardware.network_speed_test()
    }
    
    return json.dumps(info)

def return_data():
    content = get_sensor()
    info = {
        "soil_ec" : content[0],
        "soil_temp" : content[2],
        "soil_humidity" : content[4],
        "air_temp" : content[6],
        "air_humidity" : content[8],
        "sunlight" : content[10],
    }
    return json.dumps(info)    

