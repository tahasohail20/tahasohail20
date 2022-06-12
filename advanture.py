avaliable_exits =["north", "south", "east", "west"]

chosen_exit =""
while chosen_exit not in avaliable_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break

else:
    print("aren't you glad you got out of there")

asteroids = [9617, 9618, 9619, 9620, 9621, 9622, 13681]

for asteroid in asteroids:
    if asteroid == 9617:
        print("Grahamchapman")
    elif asteroid == 9618:
        print("Johncleese")
    elif asteroid == 9619:
        print("Terrygilliam")
        break
    elif asteroid == 9620:
        print("Ericidle")
    elif asteroid == 9621:
        print("Michaelpalin")
    else:
        print("Terryjones")
else:
    print("MontyPython")