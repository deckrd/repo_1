if __name__ == "__main__" :

    import RPi.GPIO as GPIO
    import time
    from DesignSpark.Pmod.HAT import createPmod

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    therm = createPmod("TC1", "JBA")

red = 21
yellow = 20
green = 16

GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

def LED_therm() :
    try:
        while True :
            cel = round(therm.readCelcius())
            if cel < 26 :
                GPIO.output(red, 0)
                GPIO.output(yellow, 0)
                GPIO.output(green, 1)
                continue
            if cel >= 26 and cel < 30 :
                GPIO.output(red, 0)
                GPIO.output(yellow, 1)
                GPIO.output(green, 0)
                continue
            else :
                GPIO.output(red, 1)
                GPIO.output(yellow, 0)
                GPIO.output(green, 0)
                continue
    except:
        print("Error on LEDs.")

    finally:
        GPIO.cleanup()
