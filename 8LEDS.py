import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) # for GPIO numbering, choose BCM

blinkCount = 5


count = 0


LEDPin1 = 18
LEDPin2 = 23
LEDPin3 = 24
LEDPin4 = 16
LEDPin5 = 20
LEDPin6 = 21
LEDPin7 = 26
LEDPin8 = 19


#setup
GPIO.setup(LEDPin1, GPIO.OUT)
GPIO.setup(LEDPin2, GPIO.OUT)
GPIO.setup(LEDPin3, GPIO.OUT)
GPIO.setup(LEDPin4, GPIO.OUT)
GPIO.setup(LEDPin5, GPIO.OUT)
GPIO.setup(LEDPin6, GPIO.OUT)
GPIO.setup(LEDPin7, GPIO.OUT)
GPIO.setup(LEDPin8, GPIO.OUT)




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

while count < blinkCount:
    GPIO.output(LEDPin4, True)
    GPIO.output(LEDPin5, True)
    GPIO.output(LEDPin6, True)
    GPIO.output(LEDPin7, True)
    GPIO.output(LEDPin8, True)
    print("LED ON")
    sleep(3)
    GPIO.output(LEDPin4, False)
    GPIO.output(LEDPin5, False)
    GPIO.output(LEDPin6, False)
    GPIO.output(LEDPin7, False)
    GPIO.output(LEDPin8, False)
    print("LED OFF")
    sleep(1)
    count +=1