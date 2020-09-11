#Variables:
ip = "192.168.1.100"
dhcp = "off"

def menu1():
    """Hovedmenu"""
    x = int(input("Hovedmenu:\n1. Tilkobling\n2. Varslinger\n3. Systeminformation\n4. Systemindstillinger"))
    return x

try:
    menunr = menu1()
except:
    pass

loop = 1
while loop == 1:
    if menunr == 1 :
        try :
            inp = int(input("Hovedmenu > Systeminformation\n1. Netværk\n2. Zoner\n3. Bus\n0. Tilbage"))
            print(inp)
        except:
            loop = 1
