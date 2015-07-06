# this script should generate a random integer of the appropriate size,
# then allow the user to take guesses until they guess correctly.
# Additional challenges:
#   1. Report the final guess count
#   2. Impose a maximum guess count
#   3. Allow the user to change the maximum using from sys import argv;
#           you'd call the script with python 06_guess_number.py <max>

#import randint from random
from random import randint
from math import log
# store a random integer as `target` (google randint for help)

print "Welcome to the number guessing game!"

min = int(raw_input("Enter a minimum value: "))
max = int(raw_input("Enter a maximum value: "))



total_tries = int(log(max-min, 2))
past_tries = 0

target = randint(min, max)
guess =  0



def hint():
	is_divisible = False
	while not is_divisible:
		n = randint(1, max)
		if target%n == 0 and n != target:
			is_divisible = True
	return ">>> Hint: the number is divisible by %d <<<" %n 


while guess!=target and past_tries < total_tries:
	print "You have tried %d times. %d tries remaining. " %(past_tries, total_tries - past_tries)
	if past_tries > total_tries*2/3 and target != 1:
		print hint()
	guess = input("------Please guess a number from %d to %d: " % (min, max))
	if guess > target:
		print "you guessed too high, pick a lower number"
		max = guess - 1
	elif guess < target:
		print "you guessed too low, pick a higher number"
		min = guess + 1
	past_tries += 1
	
if past_tries > total_tries:
	print "Sorry, you have run out of guesses. The answer was " + str(target) + "."
else:
	print "Good job! You guessed " + str(guess) + ", that is correct! It took you " + str(past_tries) + " guesses." 

# code no longer indented will run once the while loop
# is finished.  Is there anything you need to do to clean up?
# If so, put it here.
