import RPi.GPIO as GPIO
import time
from DesignSpark.Pmod.HAT import createPmod
import thingspeak
import time

from ssd_num_function import ssd_number                  # imports seven segment display script
from LED_therm_function import LED_therm                 # imports LED for thermometer script
from thingspeak_temp import measure                      # imports publish to thingspeak script 
from pir_function import pir

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

state = 0
try :
    while state == 0:
        if GPIO.input(bt0):                              # thermometer function. SSD + LED
            substate = "therm"
            while substate == "therm" :
                cel = round(therm.readCelcius())
                cel = str(cel)
                ssd_number(cel[0],"l")
                time.sleep(0.01)
                ssd_number(cel[1],"r")
                time.sleep(0.01)
                if GPIO.input(bt1):
                    substate = "pir"
                if GPIO.input(bt2):
                    substate = "hello"
                if GPIO.input(bt3):
                    substate = "end"
                    
            while substate == "pir" :
                pir()
                
            #while substate == "hello" :
            while substate == "end" :
                ssd_number(" ","l")
                ssd_number(" ", "r")
                

    
            
    else :
        print("Fault.")
        

        
finally :
    GPIO.cleanup()