choice = "-"
while True:
    if choice == "0":
        break
    elif choice in "12345":
        print("you chose {}".format(choice))
    else:
        print("Please choose your option from the list below : ")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo to swimming")
        print("4:\tHave Dinner")
        print("5:\tgo to bed")
        print("5:\tExit")
    choice = input()




