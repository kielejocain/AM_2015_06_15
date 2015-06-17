# this script should generate a random integer of the appropriate size,
# then allow the user to take guesses until they guess correctly.
# Additional challenges:
#   1. Report the final guess count
#   2. Impose a maximum guess count
#   3. Allow the user to change the maximum using from sys import argv;
#           you'd call the script with python 06_guess_number.py <max>

from random import randint
from sys import argv
script, lower_randnumber, higher_randnumber, maxguesscount = argv
# store a random integer as `target` (google randint for help)

lower_randnumber = int(lower_randnumber)
higher_randnumber = int(higher_randnumber)
maxguesscount = int(maxguesscount)
target = randint(lower_randnumber, higher_randnumber)
guess = 0
guesscount = 0


guess = int (raw_input ("What is your initial guess between %d and %d?" % (
lower_randnumber, higher_randnumber)))

while guess != target and guesscount <= maxguesscount:
    if guess < target:
        guess = int(raw_input("Sorry, guess a number that is larger."))
        guesscount += 1
        print guesscount
    elif guess > target:
        guess = int(raw_input("Sorry, guess a number that is smaller."))
        guesscount += 1
        print guesscount
if guesscount == maxguesscount:
    print "Sorry, maximum number of guesses reached. :...("

if guess == target:
    print ("Congratulations, you guessed it! It only took you %d tries!") % (
    guesscount)
    # any indented code will run over and over again
    # until the condition is no longer true

# code no longer indented will run once the while loop
# is finished.  Is there anything you need to do to clean up?
# If so, put it here.
