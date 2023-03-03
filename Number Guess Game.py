import random

print("--------NUMBER GUESS GAME--------")
print("Be careful, you have 3 chance...")

for i in range(3):
    user = int(input("Please, enter a number between 0 and 10: "))
    computer = random.randint(1,10)
    print("Computer's answer:{}".format(computer))
    if user == computer:
        print("CORRECT!!!")
        break
    else:
        print("Try again!!!")
