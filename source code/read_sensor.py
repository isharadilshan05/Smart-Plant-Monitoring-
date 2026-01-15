import serial
import time

PORT = "/dev/ttyACM0"
BAUD = 9600

ser = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)

while True:
    moisture = ser.readline().decode().strip()
    if moisture:
        print("Soil Moisture:", moisture)
    time.sleep(0.5)