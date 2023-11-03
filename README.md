# NFL-Scores
Use rpi-rgb-led-matrix to scroll current week's NFL scores on rpi and led matrix

This project is inspired and assited by many, to include https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/README.md, https://www.youtube.com/watch?v=xSwoM3M24W8, https://www.youtube.com/watch?v=omMVAtGGr_0&t=906s

Hardware used:
Raspberry Pi 4B
Adafruit RGB Matrix + RTC HAT (Soldering required!) (After the fact, I discovered Adafruit RGB Matrix Bonnet, no soldering required)
64x32 LED Matrix (HUB75 )
USB power supply for RPI
5VDC  power supply for HAT

Follow your favorite guide for connecting the hardware.
Install Raspberry Pi OS (Legacy) LITE
They have a new image downloader and SD Card creation tool at https://www.raspberrypi.com/software/operating-systems/
After creating the SD Card, and connecting all of the hardware, insert SD Card and power on the devices.
This can take some time so be patient
Log into your Pi

I took bits and pieces from all sources and smashed them together to make this work!

From https://www.youtube.com/watch?v=xSwoM3M24W8 at 8:15
```
git clone https://github.com/hzeller/rpi-rgb-led-matrix.git
```

Follow the guide on Github for Authentication Processes!

```
cd rpi-rgb-led-matrix
make build-pythong PYTHON=$(Which python 3)
sudo make install-python
cd bindings/python/smaples
```
To run the program
```
sudo python3 nflscores.py --led-cols=64 --led-rows=32 --led-slowdown-gpio=4 --led-no-hardware-pulse=1 --led-gpio-mapping=adafruit-hat
```
