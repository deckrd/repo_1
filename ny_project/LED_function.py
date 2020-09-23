import RPi.GPIO as GPIO
import time
from DesignSpark.Pmod.HAT import createPmod

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

red = 21
yellow = 20
green = 16

GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

def LED_therm() :
    
    cel = round(therm.readCelcius())
    
    if cel < 26 :
        GPIO.output(red, 0)
        GPIO.output(yellow, 0)
        GPIO.output(green, 1)
        
    if cel >= 26 and cel < 30 :
        GPIO.output(red, 0)
        GPIO.output(yellow, 1)
        GPIO.output(green, 0)
        
    else :
        GPIO.output(red, 1)
        GPIO.output(yellow, 0)
        GPIO.output(green, 0)
