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

def return_data():
    content = arduino_data.get_sensor()
    info = {
        "soil_ec" = content[0]
        "soil_temp" = content[2]
        "soil_humidity" = content[4]
        "air_temp" = content[6]
        "air_humidity" = content[8]
        "sunlight" = content[10]
    }
    return json.dumps(info)    

