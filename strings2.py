#         012345678901234

parrot = "Norwegian Blue"

print(parrot[0:6])
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])

print(parrot[10:14])
print(parrot[10:])
print(parrot[6:])
print(parrot[:6])
print(parrot[:6] + parrot[6:])
print(parrot[:])
letters = "abcdefghiklmno"
print(letters[2:7])

print(parrot[0:6])

print(parrot[-4:-2])
print(parrot[-4:12])

print(parrot[0:6:2])
print(parrot[0:6:3])

number = input("Please enter a series of numbers, using any separators you like: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

#print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))


