#This is a text based game that involves moving between interconnected boats. 
import random 



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
	
# A similar function to validate strings
	
def validate_str(input): 
	
	need_input = True
	
	while need_input:
		try:
			output = str(input)
			need_input = False
		except ValueError:
			print "please enter a valid string."
			input = raw_input(">  ")
			continue
	
	return output
	

			

#defines the Boat object which is the basis for location in this game 
class Boat(object):
		
	 #inputs are place (the boat's position), cons (a dictionary of connecting boat numbers : the conditions to move to those boats) and style (the boat's type, for flavor)
	
	def __init__(self, place, cons, style, character = None):
		
		self.connections = {} 
#		print cons # a test to ensure cons has properly been passed in
		for key in cons: # transfer the key-value pairs in the dictionary "cons" to the internal (self) dictionary "connections"
			self.connections[key] = cons[key] 
		self.position = validate_int(place) # self's position is the input int called place
		self.kind = validate_str(style) # self's kind is the input string called style
		self.person = character
	
	# def see_connections(self): # this is not used 
		# output = "Boat " + str(self.position) + " is connected to the following boats: "
		# for thing in self.connections:
			# output += str(thing) + ", " 
		# print output[:-2]
		
	def get_person(self): #probably not needed 
		if self.person is not None:
			return self.person
		else:
			self.blank_things = ["dust bunny", "mouse", "pile of old boxes."]
			return random.choice(self.blank_things)


class Player(object):
	def __init__(self):
		self.the_map = Map() # error
		#give this an attribute that is its position in the map 
		self.location = 0 

	def see_connected_boats(self):
		print "You can move to the following places. Where do you want to go? "
		current_boat = self.the_map.boats[self.location] # assign current_boat to the boat object located in the map's boats list in the position of own location
		for connection in current_boat.connections:
			
			# print "Boat number " + str(connection) + ", which is", self.the_map.boats[connection].kind 
			# print "To move to", self.the_map.boats[connection].kind, "enter the number", connection
			
			print connection, ":", self.the_map.boats[connection].kind
			# self.the_map.boats[connection].kind #eventually figure out a mechanism to make this not show the boat number. 
		
	def on_boat_actions(self):
	#stuff that should happen after moving:
		
		self.the_boat = self.the_map.boats[self.location]
		
		print "You are on boat", str(self.location) + ",", self.the_boat.kind
		self.the_person = self.the_boat.get_person()
		print "You see a", self.the_person
		print "What do you want to do?"
		print "1. talk to the", self.the_person  
		print "2. move to a different boat"
		
		action = validate_int(raw_input(" > "))
		
		self.input_needed = True
		
		while self.input_needed: 
		
			if action == 1:
				try:
					self.the_boat.person.interact()
				except:
					print "That's an odd choice."
				self.input_needed = False
			elif action == 2:
				self.move_to_boat()
				self.input_needed = False
			else: 
				print "please enter 1 or 2, then press ENTER or RETURN"
				continue 
			
		
	
	def move_to_boat(self):
		# show what the connections of this boat are
		# get the list of boats from the_map
		# get the boat at self.location
		# call see_connections on that boat. 
		self.the_boat = self.the_map.boats[self.location]
		print "You are on", self.the_boat.kind
		self.see_connected_boats()
		print "What boat do you want to move to?"
		

		
		move_to = validate_int(raw_input(">  "))


		self.the_condition = self.the_boat.connections[move_to]
		
		print "condition", self.the_condition.success_question , "is", self.the_condition.fulfilled		
		
		if move_to in self.the_boat.connections:
						
			self.the_condition = self.the_boat.connections[move_to] # trying to get the move condition associated with this connection. 
			
			print "condition", self.the_condition.success_question , "is", self.the_condition.fulfilled
			
			if self.the_condition.fulfilled:
				self.location = move_to 
				self.the_boat = self.the_map.boats[self.location]

				
				print "You have successfully moved boats"
				
				self.on_boat_actions()
				
			
			#will replace this with validation for the move condition.
			#1. determine which move condition will be used
			#  a. look at the boat we are starting at, go to that boat
			#  b. look at the connections and find the one that has been selected to move to
			#  c. find the condition associated with that connection
			#  d. evaluate to enter the if statement. 
				if self.location == self.the_map.win_boat: #tests if the most recent move has moved you to the winning boat. 
					print "Congratulations, you have reached the last boat!"
					print "You win!"
					exit(1)
			else:
				print "You can't move to this boat yet." 
		else:
			print "Sorry, you cannot move to Boat Number", move_to
class Npc(object):

	def __init__(self, desc, falsetxt, truetxt, move_cond_obj_trigger, move_cond_obj_needed):
		self.description = validate_str(desc)
		self.false_text = validate_str(falsetxt)
		self.true_text = validate_str(truetxt)

		self.move_condition_trigger = move_cond_obj_trigger #this is the move condition that is toggled by giving this person what they need
		
		self.move_condition_needed = move_cond_obj_needed # this is what needs to be true to satisfy this person so they trigger the "trigger" condition above
		
		self.have_fulfilled = False #have you given this person what they wanted? This is what determines whether that individual lets you pass. May get rid of this 
	
	def __str__(self):
		return self.description
		
	def interact(self):
		# this will be the dialog system. You talk to them and stuff happens. 
		
		if self.move_condition_needed.fulfilled == True:
			print self.true_text #they state that their need has been fulfilled and they thank you
			self.move_condition_trigger.make_fulfilled() # changes the state of the triggered condition to fulfilled
		else: 
			print self.false_text #they state that their need has not been fulfilled e.g. I'm still hungry 
			

	
	
	
class Map(object):
	
	win_boat = 6
	
	def __init__(self):
		self.boats = []
		self.handler = MoveHandler()
		self.condits = self.handler.conditions 
		
		self.people = {} #the key will be the boat they are on and the value will be the Npc object representing that person 
		
		
		#create people, add them to dictionary "people" 
		#desc, falsetxt, truetxt, move_cond_obj
		teen_girl = Npc("teenage girl", "The girl says, 'I'm so hungry! Ever since Mom started rearranging our stuff, the boats are a mess and we can't get to the pantry.' \n 'It sucks, because I had a great joke I wanted to tell you, but now I can't remember it.'", "She says, 'Ugh, I'm SOOO hungry!' \n 'Is that a cookie? Give me that!' \n *munch munch* 'Thanks! Now I remember the joke! What's brown and sticky? A stick!'", self.condits["KnowsJoke"], self.condits["HasCookie"]) #need to figure out how to get "knows_joke" and "has_cookie" object from self.condits. Maybe use indexing?  no it's a dictionary
		self.people[1] = teen_girl
		
		young_man = Npc("young man holding a baby", "He is blocking the path to the yacht. \nHe says: 'Hold on a minute, my daughter is crying.'", "You give the toy to the baby and she stops crying. \nThe young man says, 'Thanks for calming the baby, go take a cookie!'", self.condits["AlwaysYes"], self.condits["BabyCrying"])
		self.people[2] = young_man

		baker = Npc("baker wearing an apron", "She has just baked a tray of cookies. \nShe says, 'Here, have a cookie!'", "She says, 'Enjoy your cookie!'", self.condits["HasCookie"], self.condits["AlwaysYes"])
		self.people[3] = baker 
						
		little_boy = Npc("little boy", "He is blocking the bridge to the rowboat. \n'UGGGH I'M SO BORED' he moans.", "You tell him the joke you just learned. He laughs and moves out of the way.'", self.condits["AlwaysYes"], self.condits["KnowsJoke"])
		self.people[4] = little_boy
		
		midage_woman = Npc("middle-aged woman", "She says, 'Can you help me clean this mess?' \nYou spend a few minutes helping her sort through her family's belongings. \nYou find a baby toy. 'Go ahead and take that,' she says. 'My kids are much too old for it now.'", "She says, 'Thanks so much for helping me clean!'", self.condits["BabyCrying"], self.condits["AlwaysYes"])
		self.people[5] = midage_woman

		
		
		boat_cons = [[1],[0, 2],[1, 3, 5]]
		
		boat_cons = [{1: self.condits["AlwaysYes"]}, # boat 0 (beach)
					{0: self.condits["AlwaysYes"], 2: self.condits["AlwaysYes"]}, # boat 1
					{1: self.condits["AlwaysYes"], 3: self.condits["BabyCrying"], 5: self.condits["AlwaysYes"]}, # boat 2 
					{2:self.condits["BabyCrying"]}, # boat 3 eliminated 4:self.condits["AlwaysYes"]
					{6: self.condits["KnowsJoke"], 5:self.condits["AlwaysYes"]}, #boat 4 eliminated 3: self.condits["AlwaysYes"]  
					{2: self.condits["AlwaysYes"], 4:self.condits["HasCookie"]}, # boat 5  
					{4: self.condits["KnowsJoke"]}] # boat 6 
		boat_kinds = ["the beach", "a small fishing boat", "a house boat", "a dilapidated old yacht", "a sailing ship with the sails missing",  "the back part of a shipping barge", "a large rowboat"]
		
		
		for x in range(7):
			# if statement testing if there are people 
			if x in self.people: 
				a_boat = Boat(x, boat_cons[x], boat_kinds[x], self.people[x]) # error
			else: 
				a_boat = Boat(x, boat_cons[x], boat_kinds[x])
			self.boats.append(a_boat)
		
	def see_all_boats(self):
		output = "These are the boats: \n \n "
		for boat in self.boats:
			output += "\n " + str(boat.position)
			output += ", " + boat.kind
			output += ", which is home to a " + str(boat.get_person())
			output += "\n"
			
			for key in boat.connections:
				output += "----this boat is connected to boat " + str(key)
				output += " which has move condition, " + str(boat.connections[key])
				output += "\n"
		print output
		

class MoveHandler(object):
#all this does is create move conditions and store them in a list. The move conditions will be used in a dictionary where they are paired with connections between boats. 

	conditions = {}
	
	def __init__(self):

		# a standin move condition that starts out true 
		always_yes = MoveCondition()
		self.conditions["AlwaysYes"] = always_yes 
		
		# a standin move condition that starts  out false:
		starts_no = MoveCondition()
		starts_no.make_unfulfilled()
		self.conditions["StartsNo"] = starts_no
		
		
		# a standin move condition that doesn't influence enaything, for person objects needing a condition object. 
		unused = MoveCondition()
		self.conditions["Unused"] = unused
	
		baby_crying = MoveCondition("Is the baby happy?", "The baby is crying.", "The baby is happy.")
		self.conditions["BabyCrying"] = baby_crying
		has_cookie = MoveCondition("Do you have a cookie?", "You don't have a cookie.", "You have a cookie.")
		self.conditions["HasCookie"] = has_cookie
		knows_joke = MoveCondition("Do you know a joke?", "You don't know any jokes.", "You know a great joke!")
		self.conditions["KnowsJoke"] = knows_joke
		


class MoveCondition(object):

			def __init__(self, success_question = None, success_no = None, success_yes = None):

				self.success_question = ""
				self.success_no = ""
				self.success_yes = ""
			
				if success_question is None and success_no is None and success_yes is None:
					self.fulfilled = True
			# example instance: has_cookie = MoveCondition("Do you have a cookie?", "You don't have a cookie", "You have a cookie")
				else:
					self.success_question = validate_str(success_question)
					self.success_no = validate_str(success_no)
					self.success_yes = validate_str(success_yes)
				
					self.fulfilled = False 
				
			def ask_if_true(self):
				print success_question
				if self.fulfilled:
					print success_yes
					return True
				else:
					print success_no
					return False
					
			def make_fulfilled(self): 
				self.fulfilled = True
				
			def make_unfulfilled(self):
				self.fulfilled = False
				
			def __str__(self):
				return self.success_question
		
#start playing: 

print "Welcome to the boat game!"
print "You start at the beach. The goal is to move to Boat 6, a rowboat." 
print "Select options using the numbers on your keyboard and press ENTER or RETURN to proceed."
print "Have fun!"
raw_input("Press ENTER or RETURN to begin >> ")

the_player = Player() # error 

while True:
	the_player.on_boat_actions()
	
# testing of map and move conditions:	
	
# a_map = Map()
# a_map.see_all_boats()



	
#testing of move conditions and move handler

# print "Creating MoveHandler"
# the_handler = MoveHandler()

# print "Printing conditions"
# for thing  in the_handler.conditions:
	# print "Printing condition", thing
	# print thing.success_question
	# print thing.success_no
	# print thing.success_yes
	# print thing.fulfilled
	
