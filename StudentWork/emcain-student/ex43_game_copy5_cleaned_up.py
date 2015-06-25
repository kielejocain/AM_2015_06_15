#This is a text based game that involves moving between interconnected boats. 


# a function to validate input when you need an integer. This prevents type input errors from crashing the program. 
def validate_int(input): 
	
	need_input = True
	
	while need_input:
		try:
			output = int(input)
			need_input = False
		except ValueError:
			print "please enter a valid number with no decimal points"
			input = raw_input(">  ")
			continue
	
	return output
			


class Boat(object):
	
		
	def __init__(self, place, cons, style): 
		
		self.connections = []
		for item in cons:
			self.connections.append(item)
		self.position = int(place)
		self.kind = str(style)
		
	
	def see_connections(self):
		output = "Boat " + str(self.position) + " is connected to the following boats: "
		for thing in self.connections:
			output += str(thing) + ", " 
		print output[:-2]


class Player(object):
	def __init__(self):
		self.the_map = Map()
		#give this an attribute that is its position in the map 
		self.location = 0 

	def see_connected_boats(self):
		print "You can move to the following places. Where do you want to go? "
		current_boat = self.the_map.boats[self.location] 
		for connection in current_boat.connections:
			
			# print "Boat number " + str(connection) + ", which is", self.the_map.boats[connection].kind 
			# print "To move to", self.the_map.boats[connection].kind, "enter the number", connection
			
			print connection, ":", self.the_map.boats[connection].kind
			# self.the_map.boats[connection].kind #eventually figure out a mechanism to make this not show the boat number. 
		
	def move_to_boat(self):
		# show what the connections of this boat are
		# get the list of boats from the_map
		# get the boat at self.location
		# call see_connections on that boat. 
		the_boat = self.the_map.boats[self.location]
		print "You are on", the_boat.kind
		self.see_connected_boats()
		print "What boat do you want to move to?"
		
		move_to = validate_int(raw_input(">  "))
		
		
		if move_to in the_boat.connections:
			print "Yay! Guess correctly to move to Boat Number", move_to
			
			# I want to change this whole "guess number" section to a validation based on move conditions. 
			
			guess_number = validate_int(raw_input("Enter the number 42: "))
						
			if guess_number == 42:
				self.location = move_to
				print "You have successfully moved boats"
				if self.location == self.the_map.win_boat:
					print "Congratulations, you have reached the last boat!"
					print "You win!"
					exit(1)
			else:
				print "you guessed wrong, you can't cross to the new boat"
		else:
			print "Sorry, you cannot move to Boat Number", move_to
				
# class Npc(): don't need this for now 
	

class Map(object):
	
	win_boat = 6
	
	def __init__(self):
		self.boats = []
		
		boat_cons = [[1], [0,2], [3,5], [2,4], [3, 5, 6], [2,4], [3,5,6], [2,4], [4]]
		boat_kinds = ["the beach", "a small fishing boat", "a house boat", "a dilapidated old yacht", "a sailing ship with the sails missing",  "the back part of a shipping barge", "a large rowboat"]
		
		for x in range(0, 7):
			a_boat = Boat(x, boat_cons[x], boat_kinds[x])
			self.boats.append(a_boat)
		
	def see_all_boats(self):
		output = "These are the boats: "
		for thing in self.boats:
			output += " " + str(thing.position)
		print output

#start playing: 

print "Welcome to the boat game!"
print "You start at the beach. The goal is to move to Boat 6, a rowboat." 
print "Select options using the numbers on your keyboard and press ENTER or RETURN to proceed."
print "Have fun!"
raw_input("Press ENTER or RETURN to begin >> ")

the_player = Player()

while True:
	the_player.move_to_boat()

	# thing = raw_input("enter an int: ")

	# to_print = validate_int(thing)

	# print to_print