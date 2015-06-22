end = "It wasn't supposed to end like this... \n ********** " 
something = "Well, you have to do *something.*"

while True:
	print "You head to the dock hoping to catch the next boat across the sea. You notice the Royal Guard's banner flying above the dock."
	print "1. Approach the dock anyway."
	print "2. Head east along the beach."
	print "3. Head west to the cliffs."
	
	docks = raw_input("> ")
	
	if docks == "1":
		print "The Royal Guard catches you and throws you in prison."
		print end 
		
		
	elif docks == "2":
		while True:
			print "As you wander across the sand you notice what seems to be an abandoned fleet of fishing boats in the distance."
			print "1. approach the boats."
			print "2. head back to the docks."		
			
			boats = raw_input("> ")
			
			if boats == "1":
				print "You approach the boats and see that despite being in a state of disrepair, they have not been abandoned."
				print "They seem to be attached to one another with a variety of ropes, chains, hooks, seaweed and assorted detritus."

				
				approaching = raw_input("Continue... > ")
				
				print "As you draw closer, you hear the sounds of conversations, arguments, children crying, dogs barking, meals being prepared...all the hustle and bustle of city life."
				print "But where is the city?"
				
				approaching = raw_input("Continue... > ")
				
			elif boats == "2": 
				break 
			
			else:
				print something 
		
	elif docks == "3":
		print "cliffs happen"
		
	else:
		print something 