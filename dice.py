import random
randomNumber = random.randrange(1,6)
print("dice rolling...")
print randomNumber
userInput = raw_input("Would you like to roll the dice again?")
if userInput == "yes":
    print("dice rolling...")
 # while userInput == "yes"
elif userInput == "no":
    print("Dice not rolling")
else:
    print("Invalid response")
