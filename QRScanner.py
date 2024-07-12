import cv2
import time
import subprocess

# Set up camera object called Cap which we will use to find OpenCV
cap = cv2.VideoCapture(0)

# QR code detection Method
detector = cv2.QRCodeDetector()

def close_and_open_chromium(url):
    # Close all instances of Chromium
    subprocess.run(["killall", "chromium-browser"])
    time.sleep(1)  # Give it a second to close

    # Open a new Chromium tab with the specified URL
    subprocess.run(["chromium-browser", "--no-sandbox", url, stderr=subprocess.DEVNULL])

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
        cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 250, 120), 2)
        
        # Print the found data to the terminal
        if data:
            print("data found: ", data)
            if "https://www.littlegreenoffice.net/staff/littlegreenscreen.php" in data:
                close_and_open_chromium(data)
                # Pause to ensure Chromium opens properly and not rescan until a new QR code is found
                time.sleep(5)
    
    # Display the live camera feed to the Desktop on Raspberry Pi OS preview
    cv2.imshow("code detector", img)
    
    # Check if 'q' key is pressed to exit the loop
    if cv2.waitKey(1) == ord("q"):
        break
    
# When the code is stopped, close all the applications/windows that the above has created
cap.release()
cv2.destroyAllWindows()
