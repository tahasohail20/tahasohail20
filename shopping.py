shopping_list = ["Milk", "Pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
    if item == "spam":
        break
    print("Buy "+item)

for item in shopping_list:
     if item != "spam":
        print("Buy " + item)
     continue
print("Buy "+ item)

