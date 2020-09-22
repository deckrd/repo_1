import thingspeak
import time
from DesignSpark.Pmod.HAT import createPmod

therm = createPmod("TC1", "JBA")   

channel_id = 1153269
write_key = "4ZVTF64GKE82K42Q"
read_key = "QT70XUM9SQCCO2A4"

counts = dict()
cels = 0
fahrs = 0
cel_list = list()
fahr_list = list()

def measure(channel) :
    try :
        cel = therm.readCelcius()
        fahr = cel * 9 / 5
        cel = float(cel)
        fahr = float(fahr)
        cel_list.append(cel)
        fahr_list.append(fahr)
        cel_mean = sum(cel_list) / len(cel_list)
        fahr_mean = sum(fahr_list) / len(fahr_list)
        response = channel.update({"field1" : cel, "field2" : fahr, "field3" : cel_mean, "field4" : fahr_mean})
        #read = channelget({})
        #print(read)
    
    except :
        print("Connection failed.")

if __name__ == "__main__" :
    channel = thingspeak.Channel(id=channel_id, api_key=write_key)
    while True :
        measure(channel)
        time.sleep(15)
