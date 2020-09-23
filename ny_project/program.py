from startup import startup
from ssd_functions import ssd_number
from ssd_functions import ssd_letter

import time
from DesignSpark.Pmod.HAT import createPmod
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

therm = createPmod("TC1", "JBA")

red = 21
yellow = 20
green = 16

GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

aa = 4
ab = 17
ac = 27
ad = 22
ae = 5
af = 6
ag = 13
cat = 19

GPIO.setup(aa, GPIO.OUT)
GPIO.setup(ab, GPIO.OUT)
GPIO.setup(ac, GPIO.OUT)
GPIO.setup(ad, GPIO.OUT)
GPIO.setup(ae, GPIO.OUT)
GPIO.setup(af, GPIO.OUT)
GPIO.setup(ag, GPIO.OUT)
GPIO.setup(cat, GPIO.OUT)


try:
    startup()
    while True:
        cel = round(therm.readCelcius())
        cel = str(cel)
        ssd_number(cel[0],"l")
        time.sleep(0.01)
        ssd_number(cel[1],"r")
        time.sleep(0.01)
except:
    print("fuck")
    
finally:
    GPIO.cleanup()
    

