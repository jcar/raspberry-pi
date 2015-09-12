import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

flash_delay = .10

try:
    while True:
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(22,GPIO.LOW)
        time.sleep(flash_delay)
        GPIO.output(17,GPIO.LOW)
        GPIO.output(22,GPIO.HIGH)
        time.sleep(flash_delay)
except KeyboardInterrupt:
    pass
