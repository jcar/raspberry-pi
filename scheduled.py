import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

flash_delay = .10

try:
    state = "off"
    while True:
        if state == "off":
            state = "on"
            GPIO.output(17,GPIO.HIGH)
            GPIO.output(22,GPIO.HIGH)
        else:
            state = "off"
            GPIO.output(17,GPIO.LOW)
            GPIO.output(22,GPIO.LOW)
        time.sleep(5)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
