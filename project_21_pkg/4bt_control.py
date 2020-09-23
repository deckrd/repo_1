import RPi.GPIO as GPIO
import time
from DesignSpark.Pmod.HAT import createPmod
import thingspeak
import time

from ssd_num_function import ssd_number                  # imports seven segment display script
from ssd_num_function import print_therm
from LED_therm_function import LED_therm                 # imports LED for thermometer script
from thingspeak_temp import measure                      # imports publish to thingspeak script 
from pir_function import pir
from hello_function import ssd_letter

channel_id = 1153269                                     # for thingspeak
write_key = "4ZVTF64GKE82K42Q"                           # for thingspeak
read_key = "QT70XUM9SQCCO2A4"                            # for thingspeak

therm = createPmod("TC1", "JBA")                         # assigner Pmod værdi

GPIO.setwarnings(False)                                  # fjerner warnings
GPIO.setmode(GPIO.BCM)                                   # krav for breadboard

bt0 = 18
bt1 = 23
bt2 = 25
bt3 = 12

GPIO.setup(bt0, GPIO.IN)
GPIO.setup(bt1, GPIO.IN)
GPIO.setup(bt2, GPIO.IN)
GPIO.setup(bt3, GPIO.IN)

def end():
 state = 1

state = 0
while state == 0:
    if GPIO.input(bt0):                              # thermometer function. SSD + LED
        print_therm()
        continue
        
    if GPIO.input(bt1):
        pir()
        continue
        
    if GPIO.input(bt2):
        ssd_letter("h","e")
        time.sleep(0.01)
        ssd_letter("e","l")
        time.sleep(0.01)
        ssd_letter("l","l")
        time.sleep(0.01)
        ssd_letter("l","o")
        time.sleep(0.01)
        continue
    
