import random
randomNumber = random.randrange(0,100)
print("The random number has been generated")
#guessed = False
while guessed==False:
     userInput = int(input("Take your guess!"))
    if userInput==randomNumber
        guessed = True
        print("Well done!")
elif userInput>100:
    print ("below 100 please")
elif userInput<0:
    print ("Bit higher!")
elif userInput>randomNumber:
    print("try again!")
elif userInput<randomNumber:
    print ("try guessing higher!")

print("game over!")
