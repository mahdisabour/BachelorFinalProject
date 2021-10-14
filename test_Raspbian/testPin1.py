import RPi.GPIO as GPIO 
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.OUT, initial=GPIO.HIGH)
GPIO.output(6, 0)