# this script should generate a random integer of the appropriate size,
# then allow the user to take guesses until they guess correctly.
# Additional challenges:
#   1. Report the final guess count
#   2. Impose a maximum guess count
#   3. Allow the user to change the maximum using from sys import argv;
#           you'd call the script with python 06_guess_number.py <max>

from random import randint
from sys import argv

# store a random integer as `target` (google randint for help)
print "Welcome to the number guessing game."

min_guess = int(argv[1])
max_guess = int(argv[2])
target = randint(min_guess, max_guess)
correct = False
guess_count = 0
guess_limit = 10

while not correct:
    if guess_count <= guess_limit:
	    guess = int(raw_input("Enter a number between %d and %d: " % (min_guess, max_guess)))
	    if guess < target:
		print "Too low!"
		if guess > min_guess:
			min_guess = guess
	    elif guess > target:
		if guess < max_guess:
			max_guess = guess
		print "Too high!"
	    else:
		correct = True
	    guess_count += 1
    else:
	    print "You ran out of guesses. The target number was", target
	    break

if correct:
	print "Correct!"
	print "You took", guess_count, "guesses."
    
    # any indented code will run over and over again
    # until the condition is no longer true

# code no longer indented will run once the while loop
# is finished.  Is there anything you need to do to clean up?
# If so, put it here.
