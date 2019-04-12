#! /usr/bin/env python3
import os
import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P9_12", GPIO.IN, pull_up_down=GPIO.PUD_UP)# GPIO_60 on left header



try:
    while True:
        GPIO.wait_for_edge("P9_12", GPIO.FALLING)
        os.system("/sbin/shutdown -h now")
except:
    GPIO.cleanup()
#if not make sure all the pullups are in a known state

