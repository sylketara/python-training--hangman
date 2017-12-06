 #module imports
import random

name = raw_input("can I have your name please?")
print"hello" +name, "let's play hangman!"
print ""

# function to define and set a random word
def choose_word():
    wordlist = ["christmas", "elf", "santa", "rudolph"]
    chosenword = random.choice(wordlist)
    print("Random word has been chosen")
    handle_guess(chosenword, letters_used)

letters_used = ""
#define a guess
def handle_guess(chosenword, letters_used):
    #print(chosenword)
#set number of guesses on while loop
    number_of_guesses = 0
    while number_of_guesses < 15:
        number_of_guesses = number_of_guesses +1
        guess = raw_input("have a guess:")
        #making users guess always lower case
        guess = guess.lower()
        print(letters_used)
        if guess in letters_used:
            print "You have already used this letter. Try again"
        else:
            #add chosen letter to string of used letters
            letters_used = letters_used + guess
            wrong = 0
            for letter in chosenword:
                if letter in letters_used:
                    print letter,
                else:
                    print "_",
                    wrong = wrong + 1

            if guess in chosenword:
                print "You've guessed correctly!"
                if wrong == 0:
                    print "You've won!"
                    #ending while loop
                    break
            else:
                print "nope! try again"


chosenword = ""
choose_word()
