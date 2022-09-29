import hardware #라즈베리파이 하드웨어 정보 값 불러오는 모듈
import arduino_data #아두이노로부터 데이터 불러오는 모듈
import time
import json

def hardware_info():
    info =  {
        "time":time.time(),
        "uptime":"hi",#hardware.uptime_info(),
        "latitude":"dfedf", #Hardware GPS Sendsor Value 
        "longitude":"dfedf",
        "internet":hardware.network_speed_test(),#hardware.network_speed_test()
    }
    
    return json.dumps(info)

def sensor_info():
    info = {
        "soil_ec": 0, #토양 EC 센서
        "soil_temp": 0, #토양 온도 센서
        "soil_humidity": 0, #토양 습도 센서
        "air_temp": 0, #대기 온도 센서
        "air_humidity": 0, #대기 습도 센서
        "sunlight": 0, #광량 센서
    }
    
    return json.dumps(info)
