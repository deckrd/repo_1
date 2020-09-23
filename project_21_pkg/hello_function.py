import RPi.GPIO as GPIO
import time
from DesignSpark.Pmod.HAT import createPmod

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

therm = createPmod("TC1", "JBA")

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

def ssd_letter(x,y) :
    if x == "h" :
        GPIO.output(cat,1)
        GPIO.output(aa, 0)
        GPIO.output(ab, 1)
        GPIO.output(ac, 1)
        GPIO.output(ad, 0)
        GPIO.output(ae, 1)
        GPIO.output(af, 1)
        GPIO.output(ag, 1)
    if x == "e" :
        GPIO.output(cat,1)
        GPIO.output(aa, 1)
        GPIO.output(ab, 0)
        GPIO.output(ac, 0)
        GPIO.output(ad, 1)
        GPIO.output(ae, 1)
        GPIO.output(af, 1)
        GPIO.output(ag, 1)
    if x == "l" :
        GPIO.output(cat,1)
        GPIO.output(aa, 0)
        GPIO.output(ab, 0)
        GPIO.output(ac, 0)
        GPIO.output(ad, 1)
        GPIO.output(ae, 1)
        GPIO.output(af, 1)
        GPIO.output(ag, 0)
    if x == "o" :
        GPIO.output(cat,1)
        GPIO.output(aa, 1)
        GPIO.output(ab, 1)
        GPIO.output(ac, 1)
        GPIO.output(ad, 1)
        GPIO.output(ae, 1)
        GPIO.output(af, 1)
        GPIO.output(ag, 0)
    
    if y == "h" :
        GPIO.output(cat,0)
        GPIO.output(aa, 0)
        GPIO.output(ab, 1)
        GPIO.output(ac, 1)
        GPIO.output(ad, 0)
        GPIO.output(ae, 1)
        GPIO.output(af, 1)
        GPIO.output(ag, 1)
    if y == "e" :
        GPIO.output(cat,0)
        GPIO.output(aa, 1)
        GPIO.output(ab, 0)
        GPIO.output(ac, 0)
        GPIO.output(ad, 1)
        GPIO.output(ae, 1)
        GPIO.output(af, 1)
        GPIO.output(ag, 1)
    if y == "l" :
        GPIO.output(cat,0)
        GPIO.output(aa, 0)
        GPIO.output(ab, 0)
        GPIO.output(ac, 0)
        GPIO.output(ad, 1)
        GPIO.output(ae, 1)
        GPIO.output(af, 1)
        GPIO.output(ag, 0)
    if y == "o" :
        GPIO.output(cat,0)
        GPIO.output(aa, 1)
        GPIO.output(ab, 1)
        GPIO.output(ac, 1)
        GPIO.output(ad, 1)
        GPIO.output(ae, 1)
        GPIO.output(af, 1)
        GPIO.output(ag, 0)