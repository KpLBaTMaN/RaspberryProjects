import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

blinkCount = 3
count = 0
LEDPin = 22


#setup
GPIO.setup(LEDPin, GPIO.OUT)


while count < blinkCount:
    GPIO.output(LEDPin, True)
    print("LED ON")
    sleep(3)
    GPIO.output(LEDPin, False)
    print("LED OFF")
    sleep(1)
    count +=1

