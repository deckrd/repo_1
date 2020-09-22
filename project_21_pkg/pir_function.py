import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

PIR = 18
LED = 16

GPIO.setup(PIR, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

count = 0

def pir():
    if GPIO.input(PIR) :
        count += 1
        print("Motion")
        print(count)
        GPIO.output(LED,1)
        time.sleep(1)
    else :
        print("No motion")
        GPIO.output(LED,0)
        time.sleep(1)


        
    