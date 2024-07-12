import cv2
import time
import subprocess
import psutil

# Set up camera object called Cap which we will use to find OpenCV
cap = cv2.VideoCapture(0)

# QR code detection Method
detector = cv2.QRCodeDetector()

def is_chromium_running():
    # Check if Chromium is already running
    for proc in psutil.process_iter(['pid', 'name']):
        if 'chromium-browser' in proc.info['name']:
            return True
    return False

def open_chromium(url):
    if not is_chromium_running():
        subprocess.run(["chromium-browser", "--no-sandbox", url], stderr=subprocess.DEVNULL)
    else:
        # Open the URL in an existing Chromium instance
        subprocess.run(["chromium-browser", "--no-sandbox", "--new-tab", url], stderr=subprocess.DEVNULL)

# Infinite loop to keep your camera searching for data at all times
while True:
    # Method to get an image from the QR code
    _, img = cap.read()

    # Method to read the QR code by detecting the bounding box coords and decoding the hidden QR data 
    data, bbox, _ = detector.detectAndDecode(img)

    # Draw a blue box around the data and write the data on the image
    if bbox is not None:
        for i in range(len(bbox)):
            cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i + 1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
        cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[
