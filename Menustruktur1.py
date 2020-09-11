#Dette er et program til bygge videre på, hvis man skal bruge en menu i sit Pythonprogram
def prmenu():
    print("1) +")
    print("2) -")
    print("3) *")
    print("4) /")
    print("5) stop program")

prmenu()
Menunr=int(input("Vælg et nr mellem 1 - 4 og 5 for stopper programmet."))
wh=1

while wh==1:
    if Menunr == 1:
        # Her skal det kode sættes ind som skal udføre et eller andet
        print("du har valgt nr. 1) +")
        tal1=int(input("Tast første tal"))
        tal2 =int(input("tast næste tal"))
        sum=tal1+tal2
        print(tal1,"+",tal2,"=",sum)
        prmenu()
        Menunr=int(input("vælg et nr"))

    if Menunr == 2:
         # Her skal det kode sættes ind som skal udføre et eller andet
        print("du har valgt 2) -")
        prmenu()
        tal1=int(input("tast første tal"))
        tal2=int(input("tast næste tal"))
        sum=tal1-tal2
        print(tal1,"-",tal2,"=",sum)
        prmenu()
        menunr=int(input("vælg et nr"))

    if Menunr == 3:
        # Her skal det kode sættes ind som skal udføre et eller andet
        print("du har valgt 3) *")
        tal1=int(input("tast første tal"))
        tal2=int(input("tast næste tal"))
        sum=tal1*tal2
        print(tal1,"*",tal2,"=",sum)
        prmenu()
        Menunr=int(input("Vælg et nr"))

    if Menunr == 4:
        # Her skal det kode sættes ind som skal udføre et eller andet
        print("du har valgt 4) /")
        tal1=int(input("tast første tal"))
        tal2=int(input("tast næste tal"))
        sum=tal1/tal2
        print(tal1,"/",tal2,"=",sum)
        Menunr=int(input("Vælg nr. 5 for at stoppe"))
    if Menunr == 5:
        print("Nu stopper programmet!!!")
        wh=2

