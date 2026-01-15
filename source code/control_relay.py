import serial
import time

PORT = "/dev/ttyACM0"
BAUD = 9600

ser = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)

print("Relay Control Test")
print("Type 1 = relay ON, 0 = relay OFF, q = quit")

while True:
    cmd = input("Enter command: ")

    if cmd == "1":
        ser.write(b'1')
        print("Relay ON")

    elif cmd == "0":
        ser.write(b'0')
        print("Relay OFF")

    elif cmd == "q":
        print("Exiting...")
        break
