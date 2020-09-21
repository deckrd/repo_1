import RPi.GPIO as GPIO
import time
from DesignSpark.Pmod.HAT import createPmod
import ssd_num

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

therm = createPmod("TC1", "JBA")

red = 21
yellow = 20
green = 16

GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

def therm_led() :
    while True :
        cel = round(therm.readCelcius())
        if cel < 26 :
            GPIO.output(red, 0)
            GPIO.output(yellow, 0)
            GPIO.output(green, 1)
            print("grøn")
            break
        if cel > 26 and cel < 30 :
            GPIO.output(red, 0)
            GPIO.output(yellow, 1)
            GPIO.output(green, 0)
            print("gul")
            break
        if cel > 30 :
            GPIO.output(red, 1)
            GPIO.output(yellow, 0)
            GPIO.output(green, 0)
            print("rød")
            break
            
            
while True :
    cel = round(therm.readCelcius())
    cel = str(cel)
    ssd_number(cel[0],"l")
    time.sleep(0.01)
    ssd_number(cel[1],"r")
    time.sleep(0.01)
    continue


