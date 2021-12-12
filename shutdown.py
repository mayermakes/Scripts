#!/usr/bin/env python3
 #shutdown script send to Router Via:
 #scp [options] username1@source_host:directory1/filename1 username2@destination_host:directory2/filename2

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#button is active LOW
 GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def Shutdown(channel):

    print("Shutting Down")

    time.sleep(5)

    os.system("sudo shutdown -h now")
def reboot(channel):

    print("rebooting")

    time.sleep(5)

    os.system("sudo reboot -h now")
 

#GPIO interrupt kinda thingy

GPIO.add_event_detect(2, GPIO.FALLING, callback=Shutdown, bouncetime=1000)
GPIO.add_event_detect(3, GPIO.FALLING, callback=reboot, bouncetime=1000)
 #bouncetime requires min 1s = 1000ms buttonpush

#while nothing is pressed do nothing

while 1:

    time.sleep(1)
