from random import randint

target = randint(1, 10)
guessed = False

name = raw_input ("What is your name?") 

print "Hello %r we are going to play a game." % (name)
print "Don't worry %r it's not a war game." % (name)


while not guessed:
	#if guess is not target then guess again
	guess = int (raw_input ("Guess a number from 1 to 10."))
	if guess == target: 
		guessed = True
		print "Congratulations %r you have prevented Global Nuclear War!" % (name)
		
	if guess > target:
		print "The number you picked is too high %r, try again." % (name)
		
	if guess < target:
		print "The number you picked is too low %r, try again." % (name)
		
