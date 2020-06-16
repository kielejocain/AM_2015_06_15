class Boat(object):
	
	
	#some variables
	
	def __init__(self, place, cons, kind): #will add name and type later for flavor, but not needed now. 
		#some things to do when initializing
		
		self.connections = []
		for item in cons:
			self.connections.append(item)
		# will change this to a dictionary when I add move conditions. another model would  be to have "connections" objects that have boats as attributes but I don't want to worry about that now. 
		self.position = int(place)
		#start on boat one for now. can deal with moving from the beach later
		self.kind = ""
		
		# if self.position == 0:
			# self.connections = [1]
			# self.kind = "the beach"
		# elif  self.position == 1:
			# self.connections = [0, 2]
			# self.kind = "a small fishing boat"
		# elif self.position == 2:
			# self.connections = [3, 5]
			# self.kind ="a house boat"
		# elif self.position == 3:
			# self.connections = [2, 4]
			# self.kind = "a dilapidated old yacht"
		# elif self.position == 4:
			# self.connections = [3, 5, 6]
			# self.kind = "a sailing ship with the sails missing"
		# elif self.position == 5:
			# self.connections = [2, 4]
			# self.kind = "the back part of a shipping barge"
		# elif self.position == 6:
			# self.connections = [4]
			# self.kind = "a large rowboat"
		# else:
			# print "error creating boat, wrong number input"
		
		
	#some methods
	
	def see_connections(self):
		output = "Boat " + str(self.position) + " is connected to the following boats: "
		for thing in self.connections:
			output += str(thing) + ", " 
		print output[:-2]

			
# class Engine():
	

	#is this needed or can I incorporate it into Player?

class Player(object):
	def __init__(self):
		#create a map
		print "welcome to the map!"
		#give this an attribute that is its position in the map 
		self.the_map = Map()
		
		self.position = 0 
		print "you are starting in position 0."

	def see_connected_boats(self):
		print "You are connected to the following boats:"
		current_boat = self.the_map.boats[self.position] 
		for connection in current_boat.connections:
			
			print "Boat number " + str(connection) + ", which is, self.the_map.boats[connection].kind" #eventually figure out a mechanism to make this not show the boat number. 
		
	def move_to_boat(self):
		# show what the connections of this boat are
		# get the list of boats from the_map
		# get the boat at self.position
		# call see_connections on that boat. 
		the_boat = self.the_map.boats[self.position]
		print "You are on", the_boat.kind
		self.see_connected_boats()
		print "What boat do you want to move to?"
		
		need_input = True 
		
		while need_input:
			
			move_input = raw_input("> ") #eventually need to handle case of not entering an int. 

			try:
				move_to = int(move_input)
				need_input = False
			except:
				print "please enter the number of a boat you want to move to."
				continue
		
		
		if move_to in the_boat.connections:
			print "Yay! Guess correctly to move to Boat Number", move_to
			guess_number = int(raw_input("Enter the number 42: "))
			if guess_number == 42:
				self.position = move_to
				print "You have successfully moved boats"
				if self.position == self.the_map.win_boat:
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
		
		for x in range(0, 7): # move the boat connection setup to here 
			
			cons = [] 
			kind = ""
			
			if x == 0:
				cons = [1]
				kind = "the beach"
			elif  x == 1:
				cons = [0, 2]
				kind = "a small fishing boat"
			elif x == 2:
				cons = [3, 5]
				kind ="a house boat"
			elif x == 3:
				cons = [2, 4]
				kind = "a dilapidated old yacht"
			elif x == 4:
				cons = [3, 5, 6]
				kind = "a sailing ship with the sails missing"
			elif x == 5:
				cons = [2, 4]
				kind = "the back part of a shipping barge"
			elif x == 6:
				cons = [4]
				kind = "a large rowboat"
			
			a_boat = Boat(x, cons, kind)
			self.boats.append(a_boat)
			
		print "creating map..."

	def see_all_boats(self):
		output = "These are the boats: "
		for thing in self.boats:
			output += " " + str(thing.position)
		print output

#the_map = Map()
#the_map.see_all_boats()

the_player = Player()
while True:
	the_player.move_to_boat()