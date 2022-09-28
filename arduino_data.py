from pyfirmata import *

board = Arduino('/dev/ttyACM0')
seri = serial.Serail(board, baudrate=9600,timeout=None)
print("Serial name" + seri.name)

seri.write('get_sensor'.encode())