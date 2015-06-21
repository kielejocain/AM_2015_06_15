from sys import exit

#treasures = ["Longbow", "Sword", "Shield"]

#print ("Treasure_Choice %d: %r") % (index +1, treasure)

def treasure_room ():
	"This room is full of treasures. Which item do you take?"
	
	treasure = raw_input(">")

	if treasure == "1":
	print "The longbow emanates magic. Too bad you don't have any arrows."for index, treasure in enumerate(treasures): 
	