# **Huzzah32 ESP32: PWM Sounds using Micropython**

## **1. Preliminary Preparations:**

If unsure to flash the firmware on ESP32 and setting up Micropython, please follow this tutorial - [Huzzah32 ESP32: Micropython Setup](http://kentarotanaka.com/huzzah32-esp32-micropython-setup/)

## **2. Tested Environment:**

- macOS Monterey Version 12.4
- [Python3.9.5](https://www.python.org/downloads/release/python-395/)
- ESP32 Firmware: [v1.19.1](https://micropython.org/download/esp32/)

## **3. Required Materials:**

- [Adafruit HUZZAH32 – ESP32 Feather Board](https://www.adafruit.com/product/3405)
- [Surface Transducer](https://www.adafruit.com/product/1784)

## **4. Required Packages:**

```
pip3 install adafruit-ampy
pip3 install esptool
```

## **5. Hardware Connection:**

![Image](https://github.com/kntnk/esp32/blob/main/images/esp32_pwmsound.png?raw=true)

| ESP32 Pin | Transducer Pin |
| --------- | -------------- |
| Pin 33    | (+) Pin        |
| Ground    | (-) Pin        |


## **6. Usage:**

On macOS, please check the serial port of the Huzzah32 ESP32 board and export shell variable as environment variable as follows.
```
ls /dev/tty.*
export AMPY_PORT=/dev/tty.usbserial-XXXXXXXX
```

Once done with flashing the firmware onto ESP32 and setting up Micropython, simply execute as follows.
```
ampy run pwmsound.py
```

## **7. Demo Video:**

[![Watch the Video](https://img.youtube.com/vi/vzBmyRrgDSk/0.jpg)](https://youtu.be/vzBmyRrgDSk)