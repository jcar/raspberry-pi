import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

flash_delay = .10

try:
    while True:
        input_state = GPIO.input(21)
        if input_state == False:
            GPIO.output(17,GPIO.HIGH)
            GPIO.output(22,GPIO.LOW)
            time.sleep(flash_delay)
            GPIO.output(17,GPIO.LOW)
            GPIO.output(22,GPIO.HIGH)
            time.sleep(flash_delay)
        else:
            GPIO.output(17,GPIO.LOW)
            GPIO.output(22,GPIO.LOW)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
