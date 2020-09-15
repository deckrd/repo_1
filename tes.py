import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

GPIO.setup(17, GPIO.OUT) # output green
GPIO.setup(27, GPIO.OUT) # output yellow
GPIO.setup(22, GPIO.OUT) # output red
# Initial state for LEDs:
print("Testing RF out, Press CTRL+C to exit")

try:
    for i in range(50):
        GPIO.output(22, True)
        time.sleep(2)
        GPIO.output(27, True)
        time.sleep(1)
        GPIO.output(22, False)
        GPIO.output(27, False)
        GPIO.output(17, True)
        time.sleep(4)
        GPIO.output(17, False)
        GPIO.output(27, True)
        time.sleep(0.5)
        GPIO.output(27, False)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    print("Keyboard interrupt")

except:
    print("some error") 

finally:
    print("clean up") 
    GPIO.cleanup() # cleanup all GPIO 