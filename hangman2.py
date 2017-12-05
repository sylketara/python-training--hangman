 #module imports
import random

name = raw_input("can I have your name please?")
print"hello" +name, "let's play hangman!"
print ""
#print"Take a guess!"

# function to define and set a random word
def choose_word():
    wordlist = ["christmas", "elf", "santa", "rudolph"]
    chosenword = random.choice(wordlist)
    print("Random word has been chosen")
    handle_guess(chosenword)

#define a guess
def handle_guess(chosenword):
    print(chosenword)
#set number of guesses on while loop
    number_of_guesses = 0
    while number_of_guesses < 10:
        number_of_guesses = number_of_guesses +1
        guess = raw_input("have a guess:")
        print(letters_used)
        if guess in letters_used:
            print "You have already used this letter. Try again"
        else:
            if guess in chosenword:
                print "You've guessed correctly! Guess some more"
            else:
                print "nope! try again"
            if number_of_guesses > 10:
                print "You've lost!"




letters_used = ""
chosenword = ""
choose_word()
