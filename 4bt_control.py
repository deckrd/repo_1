import RPi.GPIO as GPIO
import time
from DesignSpark.Pmod.HAT import createPmod
import thingspeak
import time

from .ssd_num_function import ssd_num_function                    # imports seven segment display script
import LED_therm_function.py                    # imports LED for thermometer script
import thingspeak_temp.py                        # imports publish to thingspeak script 

channel_id = 1153269                          # for thingspeak
write_key = "4ZVTF64GKE82K42Q"                # for thingspeak
read_key = "QT70XUM9SQCCO2A4"                 # for thingspeak

therm = createPmod("TC1", "JBA")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

try :
    if GPIO.input(bt0):                        # thermometer function. SSD + LED
        try:
            while True :
                cel = round(therm.readCelcius())
                cel = str(cel)
                ssd_number(cel[0],"l")
                time.sleep(0.01)
                ssd_number(cel[1],"r")
                time.sleep(0.01)
                continue
        except:
            print("Error on SSD.")
        finally:
            RPIO.cleanup()

        
finally :
    GPIO.cleanup()