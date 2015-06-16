# this script should generate a random integer of the appropriate size,
# then allow the user to take guesses until they guess correctly.
# Additional challenges:
#   1. Report the final guess count
#   2. Impose a maximum guess count
#   3. Allow the user to change the maximum using from sys import argv;
#           you'd call the script with python 06_guess_number.py <max>

from random import randint

# store a random integer as `target` (google randint for help)
max_number = 100
target = randint(1, max_number)
guesses_left = 5


print "Welcome to a number-guessing game."
print "You have " + str(guesses_left) + " guesses. Use them wisely!"
guess = int(raw_input("Guess a number between 1 and " + str(max_number) 
	+ ": "))

while (guess != target) and (guesses_left > 0) :
	guesses_left -= 1
	# print "You guessed " + str(guess)
	if guess < target :
		guess = "Too low. You now have " + int(raw_input("Too low. Guess again: "))
	else :
		guess = int(raw_input("Too high. Guess again: "))

if count < max_guesses :
	print "Congratulations! You guessed " + str(target) + " correctly!"
	print "It took you " + str(count) + " tries."
else :
	print "Sorry, you've run out of guesses."

# code no longer indented will run once the while loop
# is finished.  Is there anything you need to do to clean up?
# If so, put it here.
