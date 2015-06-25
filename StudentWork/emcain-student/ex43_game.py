# This is a text based game that involves moving between interconnected boats. 

# It's basically a trading sequence game; you're talking to characters to determine what they want, so you can help them and they can give you something you need to continue. It's my first Python program. I hope you like it!

# This game was written in 2015 by Emily Cain (github.com/EMCain; emcain.net) 

# Protected by Attribution-ShareAlike 4.0 International, see https://creativecommons.org/licenses/by-sa/4.0/ for details. 

    # Attribution - You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

    # ShareAlike - If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

    # No additional restrictions - You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

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
		
	 #inputs are place (the boat's position), cons (a dictionary of connecting boat numbers : the conditions to move to those boats)  style (the boat's type, for flavor), and character (the person who is on the boat; None by default.)
	
	def __init__(self, place, cons, style, character = None):
		
		self.connections = {} 
		for key in cons: # transfer the key-value pairs in the dictionary "cons" to the internal (self) dictionary "connections"
			self.connections[key] = cons[key] 
		self.position = validate_int(place) # self's position is the input int called place
		self.kind = validate_str(style) # self's kind is the input string called style
		self.person = character
		
	def get_person(self): # used when a string describing the person is needed. Npc has a custom __str__method so you can use it this way.  
		if self.person is not None:
			return self.person
		else:
			self.blank_things = ["dust bunny", "mouse", "pile of old boxes"] # the idea is that if no one is on the boat you see some random junk.
			return random.choice(self.blank_things)

# the Player class handles most of your actions in the game. The Map class handles most of the background stuff that needs to happen. 
class Player(object):
	def __init__(self):
		self.the_map = Map() 
		self.location = 0 # your current position; the number refers to a boat. 

	def see_connected_boats(self):
		print "You can move to the following places."
		current_boat = self.the_map.boats[self.location] # assign current_boat to the boat object located in the map's boats list in the position of own location
		for connection in current_boat.connections:		
			print connection, ":", self.the_map.boats[connection].kind
		
	def on_boat_actions(self): # this must be run in a loop for the game to work. 
		
		self.the_boat = self.the_map.boats[self.location]
		
		raw_input("Continue >> ") # exists simply to slow down the flow of text. Otherwise it gets overwhelming. 
		print "\n"
		print "You are on " + self.the_boat.kind + "."
		self.the_person = self.the_boat.get_person() # the person (Npc) who's on the boat
		print "You see a", str(self.the_person) + ".\n" # will show some random junk like 'pile of old boxes' if there's no person
		print "What do you want to do?"
		print "1. talk to the", self.the_person  
		print "2. move to a different boat"
		
		action = validate_int(raw_input(" > ")) # ensures input is an integer and asks for new  input if it's not 
		
		self.input_needed = True
		
		while self.input_needed: 
		
			if action == 1:
				try:
					self.the_boat.person.interact() # starts a conversation with the person 
				except:
					print "That's an odd choice.\n" # this happens if you try to talk to the inanimate object that's displayed if there's no person. 
				self.input_needed = False
			elif action == 2:
				self.move_to_boat()
				self.input_needed = False
			else: 
				print "please enter 1 or 2, then press ENTER or RETURN"
				action = validate_int(raw_input(" > ")) # asks for new input and returns to the top of this while loop
				continue 
			
		
	# performs various tests to see if moving is possible, moves if possible, if not tells you why. Tests if the move causes you to win, and if so ends game
	def move_to_boat(self): 
	
		self.the_boat = self.the_map.boats[self.location] # creates the_boat attribute (if needed) and assigns it the boat you're on 
		self.see_connected_boats()
		
		print "Where do you want to go?"

		move_to = validate_int(raw_input(">  "))
			
		if move_to in self.the_boat.connections: # tests if the requested boat is connected to your current one 
		
			# gets the MoveCondition object associated with your current boat and the one you want to move to 
			self.the_condition = self.the_boat.connections[move_to] 
						
			# next uses the MoveCondition object to determine if you have done the in-game task needed to make this move. 			
			if self.the_condition.fulfilled: 
				self.location = move_to 
				self.the_boat = self.the_map.boats[self.location]
				
				print "\nYou cross a narrow rope bridge.\n"

				if self.location == self.the_map.win_boat: # tests if the most recent move has moved you to the winning boat. 
					print "Congratulations, you have reached the last boat!\n"
					print "~~~~~~~~~~~~~~~~~~~~You win!~~~~~~~~~~~~~~~~~~~~\n"
					print "< ('o'<) ( '-' ) (>^o^)> v( ^.' )v < (' .' )> < ('.'<) ( '.^ ) (>^.^)> v( 0.0 )v < (' .' )>\n" # does a little dance 
					exit(1)
					
			else:
				print "You can't move to this boat yet, because", str(self.the_condition.success_no) # if a MoveCondition prevents you from moving to this boat, this happens to explain why. 
		else:
			print "Sorry, you cannot move to Boat Number", move_to, "because it is not connected to this boat."


# MoveCondition objects are the basis of this game's logic system. They determine whether you can take actions or not. 
# If there's no restriction on an action, use the default MoveCondition object with no parameters, which I have called below as always_yes. 
# success_question is a question you're trying to answer with this MoveCondition.  
# success_no describes what happens if the answer is no; success_yes describes what happens if the answer is yes. 
# All 3 parameters are strings and only matter for story purposes; they don't affect how the object functions. 
class MoveCondition(object):

			def __init__(self, success_question = None, success_no = None, success_yes = None):

				self.success_question = ""
				self.success_no = ""
				self.success_yes = ""
			
				if success_question is None and success_no is None and success_yes is None: #default object 
					self.fulfilled = True

				else:
					self.success_question = validate_str(success_question)
					self.success_no = validate_str(success_no)
					self.success_yes = validate_str(success_yes)
				
					self.fulfilled = False 
				
			# I suppose it would make sense to have variations on this to make it unfulfilled or the opposite of whatever it is currently,
			# but I don't use them in this game so I haven't added them. 
			def make_fulfilled(self): 
				self.fulfilled = True

			def __str__(self):
				return self.success_question

#all this does is create move conditions and store them in a list. 
# The move conditions will be used in a dictionary where they are paired with connections between boats. 
class MoveHandler(object):

	conditions = {}
	
	def __init__(self):

		# a stand-in move condition that starts out true 
		always_yes = MoveCondition()
		self.conditions["AlwaysYes"] = always_yes 
		
		baby_crying = MoveCondition("Is the baby happy?", "the baby's dad is blocking the way, and won't move until she stops crying.", "The baby is happy.")
		self.conditions["BabyCrying"] = baby_crying
		has_cookie = MoveCondition("Do you have a cookie?", "you don't have a cookie.", "You have a cookie.")
		self.conditions["HasCookie"] = has_cookie
		knows_joke = MoveCondition("Do you know a joke?", "the bored little boy is sprawled out in front of the bridge.", "You know a great joke!")
		self.conditions["KnowsJoke"] = knows_joke

			
# There's a lot going on here. This is the non-player character class. 
	# Here are the inputs: 
	# desc is the description of the person, such as "a teenage girl."
	# falsetxt is what the character says before they have gotten what they want. If the person doesn't want you to do anything besides talk to them, this is never used. 
	# truetxt_first is what the character says the first time you talk to them after getting/doing the thing they want. For characters that don't want anything this is the first thing they say to you. 
	# truetxt_have_talked is what they say all other times after getting what they want; it's usually shorter and involves thanking you. 
	# move_cond_obj_trigger is the MoveCondition this character has control over. 
	# move_cond_obj_needed is the MoveCondition representing what this character wants. 
	
class Npc(object):

	def __init__(self, desc, falsetxt, truetxt_first, truetxt_have_talked, move_cond_obj_trigger, move_cond_obj_needed):
		self.description = validate_str(desc)
		self.false_text = validate_str(falsetxt)
		self.true_text_first = validate_str(truetxt_first)
		self.true_text_have_talked = validate_str(truetxt_have_talked)

		self.move_condition_trigger = move_cond_obj_trigger #this is the move condition that is toggled by giving this person what they need
		
		self.move_condition_needed = move_cond_obj_needed # this is what needs to be true to satisfy this person so they trigger the "trigger" condition above
				
		self.have_talked = False # have you talked to this person before? No. 
	
	def __str__(self):
		return self.description
		
	def interact(self):
		# this will be the dialog system. You talk to them and stuff happens. 
		
		if self.move_condition_needed.fulfilled == True:
			if self.have_talked:
				print "\n", self.true_text_have_talked, "\n" # their need has been fulfilled and they remember you. 
			else:
				print "\n", self.true_text_first, "\n" #they state that their need has been fulfilled and they thank you
				self.move_condition_trigger.make_fulfilled() # changes the state of the triggered condition to fulfilled
				self.have_talked = True 
		else: 
			print "\n", self.false_text, "\n"			#they state that their need has not been fulfilled e.g. I'm still hungry 
				
	
class Map(object):
	
	win_boat = 6
	
	def __init__(self):
		self.boats = []
		self.handler = MoveHandler()
		self.condits = self.handler.conditions 
		
		self.people = {} #the key will be the boat they are on and the value will be the Npc object representing that person 
		
		
		#create people, add them to dictionary "people" 
		teen_girl = Npc("teenage girl", 
			"The girl says, 'I'm so hungry! Ever since Mom started rearranging our stuff, \nthe boats are a mess and we can't get to the pantry.' \n \n'It sucks, because I had a great joke I wanted to tell you, but now I can't remember it.'", 
			"She says, 'Ugh, I'm SOOO hungry!' \n\n 'Is that a cookie? Give me that!' \n\n *munch munch* \n\n'Thanks! Now I remember the joke! What's brown and sticky?' \n\n 'A stick!'", 
			"She says, 'Thanks for the cookie! Did you like my joke?", 
			self.condits["KnowsJoke"], 
			self.condits["HasCookie"])
			
		self.people[1] = teen_girl
		
		young_man = Npc("young man holding a baby",
			"He is blocking the path to the yacht. \n\nHe says: 'Hold on a minute, my daughter is crying.'", "You give the toy to the baby and she stops crying. \n\nThe young man says, 'Thanks for calming the baby, go take a cookie from the yacht!'", 
			"The baby looks happy. She's so cute!", 
			self.condits["AlwaysYes"], 
			self.condits["BabyCrying"])
		
		self.people[2] = young_man

		baker = Npc("baker wearing an apron", 
			"shouldn't happen", 
			"She has just baked a tray of cookies. \n\nShe says, 'Here, have a cookie!'", 
			"She says, 'Enjoy your cookie!'", 
			self.condits["HasCookie"], 
			self.condits["AlwaysYes"])
		
		self.people[3] = baker 
						
		little_boy = Npc("little boy", 
			"He is blocking the bridge to the rowboat. \n\n'UGGGH I'M SO BORED' he moans. \n\n'Do you know any jokes?'", 
			"You tell him the joke you just learned. He laughs and moves out of the way.", 
			"The little boy is sitting on the edge of the boat. \n\nHe says, 'I'm still bored. Do you know any more jokes?'", 
			self.condits["AlwaysYes"],
			self.condits["KnowsJoke"])
		self.people[4] = little_boy
		
		midage_woman = Npc("middle-aged woman", 
			"shouldn't happen", 
			"She says, 'Can you help me clean this mess?' \n\nYou spend a few minutes helping her sort through her family's belongings. \n\nYou find a baby toy. 'Go ahead and take that,' she says. 'My kids are much too old for it now.'",
			"She says, 'Thanks so much for helping me clean!'", 
			self.condits["BabyCrying"], 
			self.condits["AlwaysYes"])
			
		self.people[5] = midage_woman

		#connections to each boat and the logical condition needed to move between them. 
		boat_cons = [{1: self.condits["AlwaysYes"]}, # boat 0 (beach)
					{0: self.condits["AlwaysYes"], 2: self.condits["AlwaysYes"]}, # boat 1
					{1: self.condits["AlwaysYes"], 3: self.condits["BabyCrying"], 5: self.condits["AlwaysYes"]}, # boat 2 
					{2:self.condits["BabyCrying"]}, # boat 3 
					{6: self.condits["KnowsJoke"], 5:self.condits["AlwaysYes"]}, #boat 4 
					{2: self.condits["AlwaysYes"], 4:self.condits["AlwaysYes"]}, # boat 5  
					{4: self.condits["KnowsJoke"]}] # boat 6 
		
		boat_kinds = ["the beach", "a small fishing boat", "a house boat", "a dilapidated old yacht", "a sailing ship with the sails missing",  "the back part of a shipping barge", "a large rowboat"]
		
		
		for x in range(7):
			# if statement testing if there are people on a given boat 
			if x in self.people: 
				a_boat = Boat(x, boat_cons[x], boat_kinds[x], self.people[x]) 
			else: 
				a_boat = Boat(x, boat_cons[x], boat_kinds[x])
			self.boats.append(a_boat)
		
	def see_all_boats(self): # a testing function which isn't used, but it's handy so I'll leave it here. 
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
		

def play():
				
	#start playing: 
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "Welcome to the boat game!"
	print "You start at the beach. There are a number of interconnected boats. The goal is to move to Boat 6, a rowboat." 
	print "Select options using the numbers on your keyboard and press ENTER or RETURN to proceed."
	print "Have fun!"

	the_player = Player()

	while True:
		the_player.on_boat_actions()
		
play()