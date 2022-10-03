from pyfirmata import *
import time

board = Arduino('/dev/ttyACM0') #시리얼 포트 지정
seri = serial.Serail(board, baudrate=9600,timeout=None) #시리얼 포트 설정
print("Serial name" + seri.name)#시리얼 포트 이름 출력

def get_sensor():
    seri.write('get_sensor'.encode()) #시리얼 포트에 데이터 전송
    time.sleep(1) #1초 대기
    content = seri.readline() #시리얼 포트에서 데이터 수신
    return content
