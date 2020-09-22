from DesignSpark.Pmod.HAT import createPmod
therm = createPmod("TC1", "JBA") 

counts = dict()
cels = 0
fahrs = 0
cel_list = [0]
fahr_list = [0]

while True:
    cel = therm.readCelcius()
    fahr = cel * 9 / 5
    cel = float(cel)
    fahr = float(fahr)
    cel_list.append(cel)
    fahr_list.append(fahr)
    cel_mean = sum(cel_list) / len(cel_list)
    fahr_mean = sum(fahr_list) / len(fahr_list)
    print(fahr_mean)
    print(cel_mean)
    #read = channelget({})
    #print(read)
