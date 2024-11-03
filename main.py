import random
x = int(input("Enter a Minmum Number: "))
y = int(input("Enter a Maximum Number: "))

if (type(x and y) == int):
    print('good')
else:
    print("galti na karo")

randomNumber = random.randint(x, y)
print(randomNumber)