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

target = randint(1,100)
guess = 0
prompt = '>'
count = 0
correct = False 
max = int(argv[1])

print "Guess a number between 1 and 100."


while guess != target and count < max:
	guess = int(raw_input(prompt))
	count += 1	
	if guess < target: 
		print "sorry %s is the wrong number, guess higher." % guess
		
	if guess > target:	
		print "sorry %s is the wrong number, guess lower" % guess
		
	if guess == target:
		correct = True
		break

if correct:
	print "Correct! %d is the right number!" % guess
else: 
	print "You've run out of guesses! The right answer was %d." % target




    # any indented code will run over and over again
    # until the condition is no longer true

# code no longer indented will run once the while loop
# is finished.  Is there anything you need to do to clean up?
# If so, put it here.