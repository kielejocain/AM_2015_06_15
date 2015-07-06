have_seen_boats = False


def end():
	print "It wasn't supposed to end like this..."
	print "*" * 40
	print "...everyone deserves a second chance."
	raw_input("Take it. >> ")
	start()

def something():
	print "Well, you have to do *something.*"
	

def start(): 
			
	print "You head to the dock hoping to catch the next boat across the sea. You notice the Royal Guard's banner flying above the dock."
	print "1. Approach the dock anyway."
	print "2. Head east along the beach."
	print "3. Head west to the cliffs."
	
	docks = raw_input("> ")
	
	if docks == "1":
		guard()
		
		
	elif docks == "2":
		beach()
	
	elif docks == "3":
		cliffs()
		
	else:
		something() 
		start()
		
def guard():
		print "The Royal Guard catches you and throws you in prison."
		end()

def cliffs():
	
	print "You hike up a gradual, grassy slope to get to the top of the cliffs."
	print "1. That was a nice hike! Go back down to the beach." 
	print "2. Continue up to the cliffside."
	
	cliff_choice = raw_input("> ")
	
	if cliff_choice == "1":
		"You head back down the hill, being careful not to stumble on the shifting sand."
		start()
		
	elif cliff_choice == "2":
		cliffside()
		
	else:
		something()
		cliffs()
		
def cliffside():
	print "You have an excellent view of the sparkling ocean to your right, and the forested hills stretching down to the left."
	print "You see the docks beneath you. Royal Guards are everywhere!"
	print "A large boat approaches. You think, 'I need to get on a boat like that...' "
	print "...but how? It's not safe down there."
	raw_input("Look farther down the beach. >>  ")
	print ("You can't quite make out what it is down there.")
	print ("Some wood platforms, like abandoned docks? Or perhaps a floating bridge?")
	print ("It's hard to tell with all the sunlight sparkling on the water.")
	have_seen_boats = True
	print have_seen_boats 
	print ("1. Move closer to the edge for a better look.")
	print ("2. Go back down to the beach.")
	
	cliffside_choice = raw_input("> ")
	
	if cliffside_choice == "1":
		print "Oops!"
		print "That ground wasn't as sturdy as it looks."
		print "You tumble down the side of the cliff, trying in vain to grab a root or piece of grass growing from the cliffside."
		end()
		
	elif cliffside_choice == "2":
		print "You find the narrow trail you used to climb the hill and proceed back down to the beach."
		start()
	
	else:
		something()
		cliffside()
		
def beach():

	print "As you wander across the sand you notice what seems to be an abandoned fleet of fishing boats in the distance."
	print have_seen_boats
	if have_seen_boats:
		print "...it's that odd series of platforms you saw before!"
	print "1. approach the boats."
	print "2. head back to the docks."		
	
	boats = raw_input("> ")
	
	if boats == "1":
		approach_boats()
		
	elif boats == "2": 
		start()
	
	else:
		something()
		beach()
		
def approach_boats():
	print "You approach the boats and see that despite being in a state of disrepair, they have not been abandoned."
	print "They seem to be attached to one another with a variety of ropes, chains, hooks, seaweed and assorted detritus."
	
	approaching = raw_input("Continue... >> ")
	
	print "As you draw closer, you hear the sounds of conversations, arguments, children crying, dogs barking, meals being prepared...all the hustle and bustle of city life."
	print "But where is the city?"
	
	approaching = raw_input("Approach the boats. >> ")


	
	
print "Welcome to the Beach Segment of this game."
print "When you see >, enter the number of your choice followed by 'enter' or 'return.'"
print "When you see >>, press 'enter' or 'return' to continue."
raw_input("Ok... >>  ")
print "Good luck!"
start()