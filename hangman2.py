# module imports
import random

# function to define and set a random word
def choose_word():
    wordlist = ["christmas", "elf", "santa", "rudolph"]
    chosenword = random.choice(wordlist)
    print("Random word has been chosen")
    print(chosenword)

#define a guess
def handle_guess():
    guess = raw_input
    while number_of_guesses < 10:
        #guess = raw_input ("Start guessing!")
        if guess in chosenword and not in letters_used:
            print "You've guessed correctly! Guess some more"
        elif guess not in chosenword and not in letters_used:
            print "nope! try again"


#based on user input, if statements if guess is true or false









choose_word()
