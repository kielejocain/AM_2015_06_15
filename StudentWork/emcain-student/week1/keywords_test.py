# keywords test

import random;

print("Welcome to the Python Keywords quiz.")
print("This is based on the list of keywords at http://learnpythonthehardway.org/book/ex37.html.")
print("For the given definition, please enter the corresponding word.")

# access the file "keywords.txt"

the_file = open("keywords.txt")

# create a dictionary with keys as the first word per line of keywords.text and values as the rest of the string

words = {}
	# loop over the lines of the file
	
for line in the_file:
	entry = line.split("\t", 1) #tab, not space 
	words[entry[0]] = entry[1]
		
	# split the first word from the rest of the line
	# create an entry to the dictionary with the first word as the key and everything else as the value. 


# play the game -- present a random value and prompt for the key. do different things depending on the answer--delete and congratulate if correct, say "wrong" and go to different question if wrong. Do this until all items in dictionary have been deleted. 


	
right = 0
wrong = 0 

looping = True

while words and looping:
	current = random.choice(words.keys())
	guess = raw_input(words[current] + ">> ")
	if guess == current: 
		print "Good job, that is correct!"
		del words[current]
		right += 1
	else:
		print "Sorry, that is wrong. The correct answer is", current 
		wrong += 1
	print "You have answered", right, "questions right and", wrong, "questions wrong."

print "Good job! You finished the quiz with only", wrong, "wrong answers."