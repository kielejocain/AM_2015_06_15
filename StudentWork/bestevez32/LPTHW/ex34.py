animals = ['Bear', 'Python', 'Peacock', 'Kangaroo', 
'Whale', 'Platypus'] 

score = [0] 
print "Your score is currently %r " % score 

for index, animal in enumerate(animals): 
	print ("Walking_Meat %d: %s") % (index + 1 , animal) 
	
print "You steady your rifle in your hand. Bringing your eye to the\n scope you see the following animals."
print "Which do you take a shot at?"

animal = raw_input ('>') 

if animal == "1":
	print "The Bear roars on it\'s haunches and turns it\'s head toward you."
	print "Do you take another quick shot, or steady your aim?"
	print "1. Take another quick shot."
	print "2. Steady your aim and take another shot."
	print "3. Do nothing and wait to die."

	aim = raw_input ('>') 
	
	if aim == "1":
		print " Your shot veers left, completely missing the Bear. He mauls you."
		score = [0 - 1] 
		print "Your loose one point and your score is currently %r " % score 
	
	elif aim == "2":
		print "You slowly squeeze the trigger and the Bear falls dead."
		score = [0 + 1] 
		print "You gained one point, your score is currently %r " % score 
		
	elif aim == "3":
		print "As you cower waiting to die you realize that your initial shot \n never hit the Bear at all. He runs straight past you and attacks \n the tour guide instead."
		print "Your score has not changed. %r" % score 
	
del animals [0] 

for index, animal in enumerate(animals): 
	print ("Walking_Meat %d: %s") % (index + 1 , animal) 
	
print "You re-steady the rifle."
print "Which animal do you shoot at now?"

animal = raw_input ('>') 



 
	

""" 
1. The animal at 1. = python 
2. The third (3rd) animal. = peacock
3. The first (1st) animal. = bear
4. The animal at 3. = kangaroo
5. The fifth (5th) animal. = whale
6. The animal at 2. = peacock
7. The sixth (6th) animal. = platypus
8. The animal at 4. = whale 
""" 