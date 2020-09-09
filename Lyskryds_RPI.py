#Statemachine til beskrivelse af livets gang
from gpiozero import LED
from time import sleep

NSred= LED(13)
NSgul=LED(19)
NSgreen=LED(26)
EVred=LED(21)
EVyellow=LED(20)
EVgreen=LED(16)


print("Test!")
EVred.on()
sleep(1)
EVgreen.on()
sleep(1)
EVyellow.on()
sleep(1)
NSred.on()
sleep(1)
NSgreen.on()
sleep(1)
NSyellow.on()
sleep(1)
EVred.off()
EVgreen.off()
EVyellow.off()
NSred.off()
NSgreen.off()
NSyellow.off()

def redred(x):# Udgangs punkt for lyskrydset
    if x=="NS": #Hvis lyskrydset kommer fra NS skal den gå til EV
        x="EV"
        print("NS RED   EV RED")
        NSred.on()
        EVred.on()
        sleep(2)
        return EV(x)
    elif x=="EV": #Hvis lyskrydset kommer fra EV skal den gå til NS
        x="NS"
        print("NS red   EV red")
        NSred.on()
        EVred.on()
        sleep(2)
        return NS(x)
def NS(x):
    if x == "NS" :
        x = "NS RED/YELLOW":
        print("NS RED/YELLOW   EV red")
        NSred.on()
        NSyellow.on()
        sleep(2)
        return NS_green(x)

def NS_green(x):
    if x == "NS RED/YELLOW":
        x = "NS GREEN":
            print("NS GREEN    EV red")
            NSred.off()
            NSyellow.off()
            NSgreen.on()
            sleep(2)
            return NS_yellow(x)

def NS_yellow(x):
    if x == "NS GREEN":
        x = "EV":
            print("NS YELLOW    EV red")
            NSgreen.off()
            NSyellow.on()
            sleep(2)
            return redred(x)
def EV():
    if x == "EV":
        x = "ES RED/YELLOW"
        print("NS red    EV RED/YELLOW")
        ESred.on()
        ESyellow.on()
        sleep(2)
        return EV_green(x)

def EV_green():
    if x == "EV RED/YELLOW"
        x = "EV GREEN"
        print("NS red    EV GREEN")
        ESgreen.on()
        sleep(2)
        return EV_yellow(x)

def EV_yellow():
    if x == "EV GREEN"
        x = "NS"
        print("NS red    EV YELLOW")
        ESyellow.on()
        sleep(2)
        return redred()
    
state=redred(x="EV")
while state: state=redred(x="EV")
