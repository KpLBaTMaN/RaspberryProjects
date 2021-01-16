import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) # for GPIO numbering, choose BCM

blinkCount = 3


count = 0


LEDPin1 = 18
LEDPin2 = 23
LEDPin3 = 24

#setup
GPIO.setup(LEDPin, GPIO.OUT)


while count < blinkCount:
    GPIO.output(LEDPin1, True)
    GPIO.output(LEDPin2, True)
    GPIO.output(LEDPin3, True)
    print("LED ON")
    sleep(3)
    GPIO.output(LEDPin1, False)
    GPIO.output(LEDPin2, False)
    GPIO.output(LEDPin3, False)
    print("LED OFF")
    sleep(1)
    count +=1

