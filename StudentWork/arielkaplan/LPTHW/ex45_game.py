from sys import exit
from random import random, randint

# playing = True
# health = 100
# evidence = 0
# carrying = []

# ENGINE
class Engine(object):
	"""Runs game"""


	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self, player):
		# Starting scene of the game
		current_scene = self.scene_map.opening_scene()
		
		# needs loop or won't change rooms more than once
		while player.playing == True: 
			# uses returned value for next chosen scene from current scene.enter()
			next_scene_name = current_scene.enter(player)
			current_scene = self.scene_map.next_scene(next_scene_name)

		# runs new scene
		current_scene.enter(player)

# PLAYER

class Player(object):
	"""Player is an undercover lab assistant. Resuce animals
	and collect evidence without getting caught or too injured."""
	
	health_states = ["hungry", "thirsty", "tired"]

	def __init__(self, name):
		self.name = name
		self.playing = True # Continue playing
		self.health = 100
		self.evidence = 0
		self.sneak = 5
		self.max_weight = 60 
		self.carrying = [] # animals

	def pick_up_animals(self, cages):

		# Keep choosing animals
		stay = True

		while stay == True:
			print ""
			for i in range(len(cages)):
				# hiding stats for now
				print str(i + 1) + ": " + str(cages[i])

			print str(len(cages) + 1) + ": None; I'm finished."
			
			pick_up = raw_input("Which animal do you pick up? >> ")

			# check that pick_up is a number
			try :
				# switch from cardinal to ordinal #
				pick_up = int(pick_up) - 1
			except:
				print "That's not a number. Try again."
				self.pick_up_animals(cages)

			# if picking from empty cage
			if (0 <= pick_up < len(cages)) and (cages[pick_up] == "Empty Cage"):
				print "You already got that one. Pick something else."
				self.pick_up_animals(cages)

			# if valid: p/u animal & remove from cage
			elif (0 <= pick_up < len(cages)) and (
				  self.max_weight - cages[pick_up].weight >= 0):
				self.carrying.append(cages[pick_up])
				self.max_weight -= cages[pick_up].weight

				cages[pick_up].bite(self)
				cages[pick_up].scratch(self)
				print "\nYou're now carrying..." 
				for animal in self.carrying:
					print "\t" + str(animal)
				print ""
				cages[pick_up] = "Empty Cage"

			# if valid, but too heavy
			elif (0 <= pick_up < len(cages)) and (
				  self.max_weight - cages[pick_up].weight < 0):
				print "You try to lift the animal into your pack,"
				print "but you just can't carry any more!"
			
			# if choice is to leave
			elif pick_up == len(cages):
				stay = False
			else:
				print "You seem confused. You're worrying me."

# ANIMALS

class Animal(object):
	"""Parent class for test subjects."""

	def __init__(self):
		self.mutant_color = ["lime green", 
					"hot pink", 
					"subtley iridescent", 
					"purple polka-dotted"]
		self.normal_color = ["chocolate brown",
					"smooth black", 
					"white and brown spotted",
					"fluffy white",
					"gray striped"]

	def __repr__(self):
		return "Teeth: " + self.teeth + "\nClaws: " + self.claws

	def bite(self, player):
		"""if teeth > 5, coin flip if bit"""	
		if self.teeth > 5:
			if random() >= 0.5:
				player.health -= self.teeth
				print "\nThe %s bit you! You're down to %s health." % (self.name, 
					player.health)
			else:
				print "\nWhew! The %s had some scary teeth, but it didn't bite you." % (
					self.name)

	def scratch(self, player):
		"""if claws > 5, coin flip if scratched"""
		if self.claws > 5:
			if random() >= 0.5:
				player.health -= self.claws
				print "\nThe %s scratched you! You're down to %s health." % (self.name, 
					player.health)
			else: 
				print "\nWhew! The %s had some scary claws, but it didn't scratch you." % (
					self.name)


class Bunny(Animal):
	"""Smallest of animals"""
	def __init__(self):
		super(Bunny, self).__init__()
		self.name = "bunny"
		self.teeth = round(random(), 1) + randint(2, 5) # total 2-6
		self.claws = round(random(), 1) + randint(1, 4) # total 1-5
		self.weight = randint(3, 5)
		self.value = 3
		self.color = self.normal_color[randint(0, len(self.normal_color)-1)]

		# 25% chance of being a mutant
		self.mutant = (random() <= .25) 
		if self.mutant == True:
			self.teeth *= 2
			self.claws *= 1.5
			self.value *= 2
			self.color = self.mutant_color[randint(0, len(self.mutant_color)-1)]

	def __str__(self):
		return ("A " + str(self.color) + " bunny")


class Cat(Animal):
	"""Mediumest of animals."""
	def __init__(self):
		super(Cat, self).__init__()
		self.name = "cat"
		self.teeth = round(random(), 1) + randint(3, 6) # total 3-7
		self.claws = round(random(), 1) + randint(3, 7) # total 3-8
		self.weight = randint(5, 11)
		self.value = 5
		self.color = self.normal_color[randint(0, len(self.normal_color)-1)]

		# 25% chance of being a mutant
		self.mutant = (random() <= .25) 
		if self.mutant == True:
			self.teeth *= 1.5
			self.claws *= 2
			self.value *= 2
			self.color = self.mutant_color[randint(0, len(self.mutant_color)-1)]


	def __str__(self):
		return ("A " + str(self.color) + " cat")



class Dog(Animal):
	"""Largest of animals."""
	def __init__(self):
		super(Dog, self).__init__()
		self.name = "dog"
		self.teeth = round(random(), 1) + randint(4, 8) # total 4-9
		self.claws = round(random(), 1) + randint(1, 4) # total 1-5
		self.weight = randint(8, 35)
		self.value = 8
		self.color = self.normal_color[randint(0, len(self.normal_color)-1)]

		# 25% chance of being a mutant
		self.mutant = (random() <= .25) 
		if self.mutant == True:
			self.teeth *= 2
			self.value *= 2
			self.color = self.mutant_color[randint(0, len(self.mutant_color)-1)]


	def __str__(self):
		return ("A " + str(self.color) + " dog")



# SCENES

class Scene(object):
	"""Parent for scenes"""

	def enter(self, player):
		print "Not yet configured."
		exit(1)
		
# Entry door
class FrontDoor(Scene):
	"""Figure the combination code to get in the lab."""
	def enter(self, player):
		print "\nHi, %s. You're at the front door." % player.name
		print "You swipe your employee card to get in."
		return "hallway"

# Hallway
class Hallway(Scene):
	"""Lets player choose lab room"""
	def enter(self, player):

		# 25% chance you get caught
		if random() <= 0.25:
			Caught().enter(player)

		print "\nYou've made it to the hallway. Where do you go?"
		print "1: Red Lab"
		print "2: Blue Lab"
		print "3: Green Lab"
		print "4: Purple Lab"
		print "5: Go outside"

		choice = raw_input("Enter a number. >> ")

		if choice == "1":
			return "red_room"
		elif choice == "2":
			return "blue_room"
		elif choice == "3":
			return "green_room"
		elif choice == "4":
			return "purple_room"
		elif choice == "5":
			print "Ahh, fresh air!"
			return "drop_off"
		else:
			player_state = player.health_states[randint(0, 2)]

			print "You wander in circles for a while until you get %s." % (
				player_state)
			player.health -= 5
			if player.health <= 0:
				return "pass_out"
			print "Your health is now %s." % player.health
			return "hallway"

# Labs: make four instances
class Lab(Scene):
	"""docstring for Lab"""
	def __init__(self, color, cages):
		self.color = color
		self.cages = cages
		if self.cages == []:
			self.fill_cages()

	def enter(self, player):
		print "\nYou've made it to the %s Room." % self.color
		print "There are %d cages." % len(self.cages)

		player.pick_up_animals(self.cages)

		return "hallway"

	def fill_cages(self):
		"""Random 4-8 cages"""

		species = [Bunny, Cat, Dog]

		# between 4 and 8 cages
		for i in range(randint(4,8)):
			# creates a random animal in each cage
			self.cages.append(species[randint(0, 2)]())


	def leave(self):
		print "Okay, let's go."
		return "hallway"

class Drop(Scene):
	"""Drop off animals carrying outside"""
	def enter(self, player):
		# global evidence
		# pull amt of evidence out of carrying list.
		if len(player.carrying) == 0:
			print "\nYou don't have any animals! Get back in there!"
			return "front_door"
		elif len(player.carrying) == 1:
			print "\nYou only have one animal. Better than nothing."
		else: 
			print "\nYou put the animals in a safe place."

		for animal in player.carrying:
			print ("A " + str(animal.color) + " " + str(animal.name) 
				   + " is worth " + str(animal.value) + ".")
			player.evidence += animal.value
		print "You've collected %d%% of the evidence you need." % (
			player.evidence)
		print "Your health is at %d%%." % (player.health)

		# Empty player's list
		player.carrying = []
		# Refil player's max_weight
		player.max_weight = 60

		if player.evidence >= 100:
			return "win"
		else:
			print "Go back in? y/n"
			answer = raw_input(">> ")
			if answer == "y":
				print "So diligent! Your hard work will soon pay off!"
				return "front_door"
			else:
				return "give_up"


# Get caught
class Caught(Scene):
	"""The scientist found you. Can you talk yourself out of it?"""
	
	def __init__(self):
		self.phrase = [
			"\n'You're here much later than I was expecting!', the scientist says suspiciously.",
			"\n'What were you doing here again? I thought I told you to go home', the scientist says.",
			"\n'Working late? I like that ambitious spirit!' the scientist says. \n'...But ambition can be dangerous.'"
		]	
		self.action = [
			"He peers at you through his magnifying goggles.",
			"He casually pulls a spider from his unkempt hair.",
			"He twirls a syringe in his fingers."
		]

	def enter(self, player):
		print "You got caught!"
		print self.phrase[randint(0, 2)]
		print "\n" + self.action[randint(0, 2)]
		print "'What number am I thinking of?', he asks."
		number = randint(-8, 113)
		tries = 10
		# print number
		while tries != 0:
			if tries == 1:
				print "You only have one more try!"
			else:
				print "You have %d tries left." % tries
			guess = raw_input("Make a guess. >> ")

			try:
				guess = int(guess)
			except:
				print "That's not a number. Try a number."

			if guess == number:
				print "Whew, you got it! The scientist nods and wanders off."
				# continue with your business
				return "hallway"
			elif guess > number:
				print "'Too high,' he says."
			elif guess < number:
				print "'Too low,' he says."
			else:
				print "I don't know how you got here..."
			tries -= 1


		# if you run out of tries	
		if (tries == 0) and (player.sneak <= 0):
			print "At your final failure, his face darkens with suspicion."
			print ".\n.\n."
			print "He suddenly slashes at you with a scapel!"
			print "You run for the door, knowing you've failed.\n"
			exit(1)
		elif tries == 0:
			print "The scientist huffs. 'I've got my eye on you', he says."
			print "'Keep your nose clean. Or else.'"
			player.sneak -= 1
		else:
			print "You shouldn't be here."

		#return "hallway"

# End: Pass out
class PassOut(Scene):
	"""Health has reached 0. Game Over."""
	def enter(self, player):
		print "\nYou start to feel woozy..."
		print "You pass out where you stand and are found the next morning."
		print "The mad scientist fires you for sleeping on the job. You failed.\n"
		player.playing = False
		exit(1)

# End: Give up
class GiveUp(Scene):
	"""You got bored and gave up."""
	def enter(self, player):
		print "\nWhat a terrible work ethic. I'm disappointed. You lose.\n"
		player.playing = False
		exit(1)

# End: You win!
class Win(Scene):
	"""You've gathered enough evidence. You Win."""
	def enter(self, player):
		print "\nYou've got enough evidence to shut down the lab! You win!\n"
		player.playing = False
		exit(1)

# MAP
class Map(object):
	"""Creates scenes"""

	red_cages = []
	blue_cages = []
	green_cages = []
	purple_cages = []

	scenes = {
		"front_door": FrontDoor(),
		"red_room": Lab("Red", red_cages),
		"blue_room": Lab("Blue", blue_cages),
		"green_room": Lab("Green", green_cages),
		"purple_room": Lab("Purple", purple_cages),
		"drop_off": Drop(),
		"hallway": Hallway(),
		"caught": Caught(),
		"pass_out": PassOut(),
		"give_up": GiveUp(),
		"win": Win()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene
		self.opening_scene()

	def next_scene(self, scene_name):
		"""Takes you to next scene"""
		val = Map.scenes.get(scene_name)
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)

print "-" * 10
print "You're undercover at a mad scientist's animal-testing laboratory."
print "It is your task to collect enough evidence to close the lab,"
print "while not getting either arousing too much suspicion or getting"
print "too scratched up by the distressed animals you're trying to rescue."
print "-" * 10

code_name = raw_input("What is your code name? >> ")

a_map = Map("front_door")
a_player = Player(code_name)

a_game = Engine(a_map)
a_game.play(a_player)

