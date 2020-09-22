import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

bt0 = 18
bt1 = 23
bt2 = 25
bt3 = 12

GPIO.setup(bt0, GPIO.IN)
GPIO.setup(bt1, GPIO.IN)
GPIO.setup(bt2, GPIO.IN)
GPIO.setup(bt3, GPIO.IN)

while GPIO.input(bt0):
    print("test")
