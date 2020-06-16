# this script should generate a random integer of the appropriate size,
# then allow the user to take guesses until they guess correctly.
# Additional challenges:
#   1. Report the final guess count
#   2. Impose a maximum guess count
#   3. Allow the user to change the maximum using from sys import argv;
#           you'd call the script with python 06_guess_number.py <max>

from random import randint
from sys import argv

script, number_1, number_2 = argv
# turn the argv to ints
number_1 = int(number_1)
number_2 = int(number_2)

# store a random integer as `target` (google randint for help)
target = randint(number_1, number_2)

guess = 1

def guess_max(guess):
	guess_max = number_2 / 2
	if guess > guess_max:
		print "You ran out of guesses! You used ", guess, " guesses!"
	else:
		print "You have ", guess_max - guess, " guesses left."

#Ask user for initial guess
user_guess = int(raw_input("Guess a number between 1 - 10:\n"))

while user_guess != target:
	if user_guess < target:
		user_guess = int(raw_input("That was too low, guess a larger number \n"))
		guess += 1
		guess_max(guess)
	else:
		user_guess = int(raw_input("That was too high, guess a smaller number\n"))
		guess += 1
		guess_max(guess)

if user_guess == target:
	print "Congratualations! you guessed the number. It took you ", guess, " guesses!"		


