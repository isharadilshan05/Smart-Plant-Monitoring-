import cv2
import numpy as np
import time

IMAGE_PATH = "plant.jpg"

img = cv2.imread(IMAGE_PATH)
if img is None:
    print("Image not found.")
    exit()

height, width, _ = img.shape
start = time.time()

# Convert to HSV for green detection
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Range for green
lower_green = np.array([25, 40, 40])
upper_green = np.array([95, 255, 255])

mask = cv2.inRange(hsv, lower_green, upper_green)
green_ratio = np.sum(mask == 255) / (height * width)

# Decision
if green_ratio > 0.3:
    status = "HEALTHY"
else:
    status = "POSSIBLY UNHEALTHY OR DRY"

end = time.time()

print("\n===== Edge Image Analysis Result =====")
print(f"Green pixel ratio: {green_ratio:.2f}")
print(f"Estimated plant status: {status}")
print(f"Inference time: {round((end-start)*1000, 1)} ms")
