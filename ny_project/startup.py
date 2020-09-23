import RPi.GPIO as GPIO
import time
from DesignSpark.Pmod.HAT import createPmod
from ssd_functions import ssd_number
from ssd_functions import ssd_letter

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

def startup():
    GPIO.output(red, 0)
    GPIO.output(yellow, 0)
    GPIO.output(green, 0)
    ssd_letter(" ","l")
    time.sleep(0.001)
    ssd_letter(" ","r")
    time.sleep(2)
    ssd_letter("h","l")
    GPIO.output(red, 1)
    time.sleep(0.5)
    GPIO.output(red, 0)
    ssd_letter(" ","l")
    time.sleep(0.5)
    ssd_letter("e","l")
    GPIO.output(yellow, 1)
    time.sleep(0.5)
    GPIO.output(yellow, 0)
    ssd_letter(" ","l")
    time.sleep(0.5)
    ssd_letter("l","l")
    GPIO.output(green, 1)
    time.sleep(0.5)
    GPIO.output(green, 0)
    ssd_letter(" ","l")
    time.sleep(0.5)
    ssd_letter("l","l")
    GPIO.output(yellow, 1)
    time.sleep(0.5)
    GPIO.output(yellow, 0)
    ssd_letter(" ","l")
    time.sleep(0.5)
    ssd_letter("o","l")
    GPIO.output(red, 1)
    time.sleep(0.5)
    GPIO.output(red, 0)
    ssd_letter(" ","l")
    GPIO.output(red, 1)
    time.sleep(0.5)
    GPIO.output(yellow, 1)
    time.sleep(0.5)
    GPIO.output(green, 1)
    time.sleep(2)
    GPIO.output(red, 0)
    GPIO.output(yellow, 0)
    GPIO.output(green, 0)
