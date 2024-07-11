:# LittleGreenScreen
Setup instructions for LittleGreenScreen:

ENABLE CAMERA AND DOWNLOAD QRScanner.py

sudo apt-get update

sudo apt-get install python3-opencv

sudo apt-get install libqt4-test python3-sip python3-pyqt5 libqtgui4 libjasper-dev libatlas-base-dev -y

pip3 install opencv-contrib-python==4.1.0.25

sudo modprobe bcm2835-v4l2

sudo mousepad /etc/xdg/lxsession/LXDE-pi/autostart

At the bottom of the file: 

@chromium-browser --kiosk default URL
@lxterminal

Default URL: https://www.littlegreenoffice.net/staff/littlegreenscreen.php

Save and Exit to terminal

sudo nano /home/lgbc/.bashrc
Go to the last line of the script and add:

echo Running at boot 
python3 /home/lgbc/QRScanner.py

ctrl+s ctrl+x

sudo reboot
