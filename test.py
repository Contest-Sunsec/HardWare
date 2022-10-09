from pyfirmata import *
import time


seri = serial.Serial(baudrate=9600,timeout=None, port = 'COM6') #시리얼 포트 설정
print("Serial name" + seri.name)#시리얼 포트 이름 출력

res = []

def get():
    time.sleep(2)
    for i in range(0, 8):
        seri.write('g'.encode()) #시리얼 포트에 데이터 전송
        con = seri.readline() #시리얼 포트에서 데이터 수신
        con = con[:len(con)-1].decode().replace('\r', '')
        res.append(con)
        print(con)
        
get()
print(res)