import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

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

def ssd_number(x) :
    if x == 1 :
        GPIO.output(aa, 0)
        GPIO.output(ab, 0)
        GPIO.output(ac, 0)
        GPIO.output(ad, 0)
        GPIO.output(ae, 1)
        GPIO.output(af, 1)
        GPIO.output(ag, 0)
    if x == 2 :
        GPIO.output(aa, 1)
        GPIO.output(ab, 1)
        GPIO.output(ac, 0)
        GPIO.output(ad, 1)
        GPIO.output(ae, 1)
        GPIO.output(af, 0)
        GPIO.output(ag, 1)
    if x == 3 :
        GPIO.output(aa, 1)
        GPIO.output(ab, 1)
        GPIO.output(ac, 1)
        GPIO.output(ad, 1)
        GPIO.output(ae, 0)
        GPIO.output(af, 0)
        GPIO.output(ag, 1)
    if x == 4 :
        GPIO.output(aa, 0)
        GPIO.output(ab, 1)
        GPIO.output(ac, 1)
        GPIO.output(ad, 0)
        GPIO.output(ae, 0)
        GPIO.output(af, 1)
        GPIO.output(ag, 1)
    if x == 5 :
        GPIO.output(aa, 1)
        GPIO.output(ab, 0)
        GPIO.output(ac, 1)
        GPIO.output(ad, 1)
        GPIO.output(ae, 0)
        GPIO.output(af, 1)
        GPIO.output(ag, 1)
    if x == 6 :
        GPIO.output(aa, 1)
        GPIO.output(ab, 0)
        GPIO.output(ac, 1)
        GPIO.output(ad, 1)
        GPIO.output(ae, 1)
        GPIO.output(af, 1)
        GPIO.output(ag, 1)
    if x == 7 :
        GPIO.output(aa, 1)
        GPIO.output(ab, 1)
        GPIO.output(ac, 1)
        GPIO.output(ad, 0)
        GPIO.output(ae, 0)
        GPIO.output(af, 0)
        GPIO.output(ag, 0)
    if x == 8 :
        GPIO.output(aa, 1)
        GPIO.output(ab, 1)
        GPIO.output(ac, 1)
        GPIO.output(ad, 1)
        GPIO.output(ae, 1)
        GPIO.output(af, 1)
        GPIO.output(ag, 1)
    if x == 9 :
        GPIO.output(aa, 1)
        GPIO.output(ab, 1)
        GPIO.output(ac, 1)
        GPIO.output(ad, 1)
        GPIO.output(ae, 0)
        GPIO.output(af, 1)
        GPIO.output(ag, 1)
    if x == 0 :
        GPIO.output(aa, 1)
        GPIO.output(ab, 1)
        GPIO.output(ac, 1)
        GPIO.output(ad, 1)
        GPIO.output(ae, 1)
        GPIO.output(af, 1)
        GPIO.output(ag, 0)
        
for i in [0,1,2,3,4,5,6,7,8,9,] :
    ssd_number(i)
    time.sleep(0.5)

    
