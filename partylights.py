import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

#loop for 10 seconds


t_end = time.time() + 60 * 15
while time.time() < t_end:
    GPIO.output(17,GPIO.HIGH)
    GPIO.output(22,GPIO.LOW)
    time.sleep(.25)
    GPIO.output(17,GPIO.LOW)
    GPIO.output(22,GPIO.HIGH)
    time.sleep(.25)
