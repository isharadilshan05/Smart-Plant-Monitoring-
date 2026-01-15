import serial
import time
import requests

# Serial setup
PORT = "/dev/ttyACM0"
BAUD = 9600

DRY_ON_THRESHOLD = 630
WET_OFF_THRESHOLD = 670

THINGSPEAK_URL = "https://api.thingspeak.com/update"
WRITE_API_KEY = "YOUR_API_KEY_HERE"

def send_to_thingspeak(moisture, relay_state):
    try:
        payload = {
            "api_key": WRITE_API_KEY,
            "field1": moisture,
            "field2": relay_state
        }
        response = requests.post(THINGSPEAK_URL, params=payload)
        if response.status_code == 200:
            print("ThingSpeak: Sent ✓")
        else:
            print("ThingSpeak Error:", response.status_code)
    except Exception as e:
        print("Upload failed:", e)

def main():
    ser = serial.Serial(PORT, BAUD, timeout=1)
    time.sleep(2)

    relay_state = 0

    print("Starting automation")
    print("Press CTRL+C to stop\n")

    while True:
        data = ser.readline().decode().strip()
        if not data:
            continue

        try:
            moisture = int(data)
        except:
            continue

        status = ""

        # DRY → switch ON relay
        if moisture < DRY_ON_THRESHOLD:
            ser.write(b'1')
            relay_state = 1
            status = "DRY → Relay ON"

        # WET → switch OFF relay
        elif moisture > WET_OFF_THRESHOLD:
            ser.write(b'0')
            relay_state = 0
            status = "WET → Relay OFF"

        print(f"Soil Moisture: {moisture} | {status}")
        
        send_to_thingspeak(moisture, relay_state)
        time.sleep(10)

if __name__ == "__main__":
    main()
