def menu():
    inp = int(input("Hovedmenu:\n1. Tilkobling\n2. Varslinger\n3. Systeminformation\n4. Systemindstillinger"))
    return inp

ip = "192.168.1.100"
dhcp = "off"

inp = menu()

loop = 1
while loop == 1 :

    if inp == 1 :
        try:
            if inp == 1 :
                inp = int(input("Tast 1 for at tilkoble nu."))
                if inp == 1 :
                    print("Alt tilkoblet.")
                    continue
            if inp == "2" :
                inp = int(input("Tryk 1 for at se varslinger."))
                if inp == 1 :
                    print("Ingen varsler.")
                    continue
        except:
            break

    if inp == 3 :
        try :
            inp = int(input("Hovedmenu > Systeminformation\n1. Netværk\n2. Zoner\n3. Bus\n0. Tilbage"))
            if inp == 1 :
                inp = int(input("Systeminformation > Netværk\n1. IP adresse\n2. DHCP\n0. Tilbage"))
                if inp == 1 :
                    print("Netværk > IP adresse\nIP adresse:", ip)
                    inp = input("Tast # for at ændre, 0 for at gå tilbage.")
                    if inp == "#":
                        inp = input("Indtast ny IP adresse:")
                        ip = inp
                        print("Ny IP adresse:",ip)
                        inp = input("Tast 0 for at gå tilbage")
                        if inp == 0:
                            inp = 1
                    if inp == 0:
                        break
            elif inp == 2 :
                print("DHCP:", dhcp)
                loop = 2
            elif inp == 0 :
                inp = 3
                continue
        except :
            loop = 1

while loop == 2 :
    print("loop 2")
    break
