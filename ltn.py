import RPi.GPIO as GPIO
import time
from picamera import PiCamera

camera = PiCamera()
camera.start_preview()
time.sleep(2)
green_button_gpio = 14
green_button_pressed = 0
key_gpio = 15
key_armed = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(green_button_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(key_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    time.sleep(0.1)
    while GPIO.input(key_gpio) == key_armed:
        time.sleep(0.1)
        for filename in camera.capture_continuous('img{counter:03d}.jpg'):
            print('Captured %s' % filename)
            if GPIO.input(green_button_gpio) == green_button_pressed:
                print('Button Pressed')
