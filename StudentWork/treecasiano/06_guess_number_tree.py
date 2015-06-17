# this script should generate a random integer of the appropriate size,
# then allow the user to take guesses until they guess correctly.
# Additional challenges:
#   1. Report the final guess count
#   2. Impose a maximum guess count
#   3. Allow the user to change the maximum using from sys import argv;
#           you'd call the script with python 06_guess_number.py <max>

from random import randint
from sys import argv

high_number = int(argv[1])
target = randint(1, high_number)
num_guesses = 5
print "I am thinking of an integer between 1 and %d." %high_number
print "You have five tries to guess my number."
user_guess = 0

while target != user_guess and num_guesses != 0:
    print "Guesses left: %d" % num_guesses
    print " "
    user_guess = int(raw_input("What is my number? "))
    if user_guess < target:
        print "Close but no cigar. My number is higher."
    elif user_guess > target:
        print "Nope. Not it. You're too high."
    else:
        print "Bingo! You got the right number in %d tries." % num_guesses
    num_guesses -= 1

if num_guesses == 0:
    print "So sad. You have run out of guesses."
    print " "


