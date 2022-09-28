import hardware #라즈베리파이 하드웨어 정보 값 불러오는 모듈
import arduino_data #아두이노로부터 데이터 불러오는 모듈
import time
import json

def hardware_info():
    info =  {
        "time":time.time(),
        "uptime":"hi",#hardware.uptime_info(),
        "latitude":"dfedf",
        "longitude":"dfedf",
        "internet":"hi",#hardware.network_speed_test()
    }
    
    return json.dumps(info)

def sensor_info():
    info = {
        "soil_ec": 0,
        "soil_temp": 0,
        "soil_humidity": 0,
        "air_temp": 0,
        "air_humidity": 0,
        "sunlight": 0,
    }
    
    return json.dumps(info)
