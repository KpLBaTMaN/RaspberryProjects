import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) # for GPIO numbering, choose BCM




LEDPin1 = 18
LEDPin2 = 23
LEDPin3 = 24
LEDPin4 = 16
LEDPin5 = 20
LEDPin6 = 21
LEDPin7 = 26
LEDPin8 = 19

listLEDS = [LEDPin1, LEDPin2, LEDPin3, LEDPin4, LEDPin5, LEDPin6, LEDPin7, LEDPin8]

#setup Programming the lights
GPIO.setup(LEDPin1, GPIO.OUT)
GPIO.setup(LEDPin2, GPIO.OUT)
GPIO.setup(LEDPin3, GPIO.OUT)
GPIO.setup(LEDPin4, GPIO.OUT)
GPIO.setup(LEDPin5, GPIO.OUT)
GPIO.setup(LEDPin6, GPIO.OUT)
GPIO.setup(LEDPin7, GPIO.OUT)
GPIO.setup(LEDPin8, GPIO.OUT)


#Variables
num = 0
numInBinary = ""





while True:

    #Reset back to one if it goes pat 8 bits worth of numbers
    if num >= 256:
        num = 0

    numInBinary = '{0:08b}'.format(num)

   # numInBinary[0]

    for x in range(8):
        if numInBinary[x] == "1":
            GPIO.output(listLEDS[x], True)
        else:
            GPIO.output(listLEDS[x], False)

    sleep(1)
    num += 1