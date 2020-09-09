#Statemachine til beskrivelse af livets gang
from gpiozero import LED
from time import sleep
import random

NSred= LED(13)
NSyellow=LED(19)
NSgreen=LED(26)
EVred=LED(21)
EVyellow=LED(20)
EVgreen=LED(16)


#print("Test!")
#EVred.on()
#sleep(1)
#EVgreen.on()
#sleep(1)
#EVyellow.on()
#sleep(1)
#NSred.on()
#sleep(1)
#NSgreen.on()
#sleep(1)
#NSyellow.on()
#sleep(1)
#EVred.off()
#EVgreen.off()
#EVyellow.off()
#NSred.off()
#NSgreen.off()
#NSyellow.off()

def redred(x):# Udgangs punkt for lyskrydset
    if x=="NS": #Hvis lyskrydset kommer fra NS skal den gå til EV
        x="EV"
        print("NS RED   EV RED")
        NSred.on()
        EVred.on()
        NSyellow.off()
        EVyellow.off()
        NSgreen.off()
        EVgreen.off()
        sleep(2)
        return EV(x)
    elif x=="EV": #Hvis lyskrydset kommer fra EV skal den gå til NS
        x="NS"
        print("NS red   EV red")
        NSred.on()
        EVred.on()
        EVyellow.off()
        NSyellow.off()
        EVgreen.off()
        NSgreen.off()
        sleep(2)
        return NS(x)
def NS(x):
    global count
    if x == "NS" :
        x = "NS RED/YELLOW"
        print("NS RED/YELLOW   EV red")
        count = count + 1
        NSred.on()
        NSyellow.on()
        sleep(2)
        return NS_green(x)

def NS_green(x):
    global count
    if x == "NS RED/YELLOW":
        x = "NS GREEN"
        print("NS GREEN    EV red")
        count = count + 1
        NSred.off()
        NSyellow.off()
        NSgreen.on()
        sleep(2)
        return NS_yellow(x)

def NS_yellow(x):
    global count
    if x == "NS GREEN":
        x = "NS"
        print("NS YELLOW    EV red")
        count = count + 1
        NSgreen.off()
        NSyellow.on()
        sleep(2)
        return redred(x)
def EV(x):
    global count
    if x == "EV":
        x = "EV RED/YELLOW"
        print("NS red    EV RED/YELLOW")
        count = count + 1
        EVred.on()
        EVyellow.on()
        sleep(2)
        crash()
        return EV_green(x)

def EV_green(x):
    global count
    if x == "EV RED/YELLOW":
        x = "EV GREEN"
        print("NS red    EV GREEN")
        count = count + 1
        EVred.off()
        EVyellow.off()
        EVgreen.on()
        sleep(2)
        crash()
        return EV_yellow(x)

def EV_yellow(x):
    global count
    if x == "EV GREEN":
        x = "EV"
        print("NS red    EV YELLOW")
        count =  count + 1
        EVgreen.off()
        EVyellow.on()
        sleep(2)
        crash()
        return redred(x)

def crash():                 #chance for grøn/grøn
    global count
    if count > random.randrange(1, 10):
        EVred.off()
        EVyellow.off()
        EVgreen.on()
        NSred.off()
        NSyellow.off()
        NSgreen.on()
        sleep(2)
        count = 0
        return redred("NS")
    
    
count = 0
state=redred(x="EV")
while state: state=redred(x="EV")

