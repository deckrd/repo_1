import random
import time
import terninger as d6
 
def roll_dice_human():
    roll_human = random.randrange(1,7)
    return roll_human
 
def roll_dice_machine():
    roll_machine = random.randrange(1,7)
    return roll_machine
 
 
score_human = 0
score_machine = 0
 
print("Dette er et terningespil.")
print("Du spiller mod maskinen.")
print("Spillet afsluttes, når enten spiller eller maskine når 10 point.")
while score_human < 10 and score_machine < 10:
    roll_human = roll_dice_human()
    roll_machine = roll_dice_machine()
    enter = input("Tryk på enter for at slå en terning")
    if enter == '':
        roll_dice_human()
    print("...")
    time.sleep(1)
    print("Du slog en",roll_human,"'er.")
    d6.terning(roll_human)
    print("Nu er det maskinens tur.")
    print("...")
    time.sleep(1)
    roll_dice_machine()
    print("Maskinen slog en",roll_machine,"'er")
    d6.terning(roll_machine)
    if roll_human > roll_machine:
        print("Du vandt!")
        score_human = score_human + 1
    else:
        print("Du tabte.")
        score_machine = score_machine + 1
    print("""
   Score er:
   Dig:""", score_human,"CPU:", score_machine)
    print("Næste runde starter nu.")
    continue
print("Spillet er nu slut. Score er: Dig:", score_human, "CPU", score_machine)
if score_human > score_machine:
    print("Du vandt spillet!")
elif score_human == score_machine:
    print("Spillet er uafgjort.")
else:
    print("Du tabte spillet.")