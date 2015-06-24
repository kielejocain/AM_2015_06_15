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

class Assistant(object):
	"""Player is an undercover lab assistant. Resuce animals
	and collect evidence without getting caught or too injured."""
	def __init__(self, name):
		self.name = name
		self.playing = True # Continue playing
		self.health = 100
		self.evidence = 0
		self.max_weight = 60 
		self.carrying = [] # animals

	def get_injured(self, animal):
		pass

	def pick_up_animals(self, cages):
		print "\nWhich animals to rescue?"

		# Keep choosing animals
		stay = True

		while stay == True:
			for i in range(len(cages)):
				# hiding stats for now
				print str(i + 1) + ": " + str(cages[i])
			print str(len(cages) + 1) + ": None; I'm finished."
			
			pick_up = raw_input("Which animal do you pick up? >> ")

			# check that pick_up is a number
			try :
				pick_up = int(pick_up)
				# switch from cardinal to ordinal #
				pick_up -= 1

				# if picking from empty cage
				if (pick_up < len(cages)) and (cages[pick_up] == "Empty Cage"):
					print "You already got that one. Pick something else."
					self.pick_up_animals()
				# if valid: p/u animal & remove from cage
				elif 0 <= pick_up < len(cages):
					self.carrying.append(cages[pick_up])
					print self.carrying
					print "\n"
					cages[pick_up] = "Empty Cage"
				# if choice is to leave
				elif pick_up == len(cages):
					stay = False
				else:
					print "You seem confused. You're worrying me."

			except TypeError:
				print "That's not a number. Try again."
				self.pick_up_animals()


# ANIMALS

class Animal(object):
	"""Parent class for test subjects."""

	def __init__(self):
		self.teeth = random() * 10
		self.claws = random() * 10

	def __repr__(self):
		return "Teeth: " + self.teeth + "\nClaws: " + self.claws


class Bunny(Animal):
	"""Smallest of animals"""
	def __init__(self, danger):
		super(Bunny, self).__init__()
		self.name = "bunny"
		self.weight = randint(3, 5)
		self.value = 3

	def __repr__(self):
		return ("Bunny\n\tTeeth: " + str(self.teeth) + 
			    "\n\tClaws: " + str(self.claws) +
			    "\n\tValue: " + str(self.value))


class Cat(Animal):
	"""Mediumest of animals."""
	def __init__(self, danger):
		super(Cat, self).__init__()
		self.name = "cat"
		self.weight = randint(5, 11)
		self.claws *= 1.5
		self.value = 5

	def __repr__(self):
		return ("Cat\n\tTeeth: " + str(self.teeth) + 
			    "\n\tClaws: " + str(self.claws) +
			    "\n\tValue: " + str(self.value))


class Dog(Animal):
	"""Largest of animals."""
	def __init__(self, danger):
		super(Dog, self).__init__()
		self.name = "dog"
		self.weight = randint(8, 35)
		self.teeth *= 2.0
		self.claws /= 2.0
		self.value = 8

	def __repr__(self):
		return ("Dog\n\tTeeth: " + str(self.teeth) + 
			    "\n\tClaws: " + str(self.claws) +
			    "\n\tValue: " + str(self.value))


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
		print "I'm gonna assume you got the code right. Lucky you."
		return "hallway"

# Hallway
class Hallway(Scene):
	"""Lets player choose lab room"""
	def enter(self, player):
		print "\nYou've made it to the hallway. Where do you go?"
		print "1: Red Room"
		print "2: Blue Room"
		print "3: Green Room"
		print "4: Purple Room"
		print "5: Go outside"

		choice = raw_input(">> ")
		if choice == "1":
			print "You pick the Red Room"
			return "red_room"
		elif choice == "2":
			print "You pick the Blue Room"
			return "blue_room"
		elif choice == "3":
			print "You pick the Green Room"
			return "green_room"
		elif choice == "4":
			print "You pick the Purple Room"
			return "purple_room"
		elif choice == "5":
			print "Ahh, fresh air!"
			return "drop_off"
		else:
			print "You wander in circles for a while."
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

		# arguments currently don't mean anything
		species = [Bunny(1), Cat(2), Dog(3)]

		# between 4 and 8 cages
		for i in range(randint(4,8)):
			# creates a random animal in each cage
			self.cages.append(species[randint(0, 2)])


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
			print str(animal.name) + " is worth " + str(animal.value)
			player.evidence += animal.value
		print "You've collected %d%% of the evidence you need." % (
			player.evidence)

		# Empty player's list
		player.carrying = []

		if player.evidence >= 100:
			return "You've got enough evidence to shut down the lab! You win!"
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
	def enter(self, player):
		print "You got caught"
		pass

# End: Pass out
class PassOut(Scene):
	"""Health has reached 0. Game Over."""
	def enter(self, player):
		print "\nA valiant effort, but the animals did too much damage to you."
		print "You pass out in the lab and are found the next morning."
		print "The mad scientist fires you for sleeping on the job."
		player.playing = False
		exit(1)

# End: Give up
class GiveUp(Scene):
	"""You got bored and gave up."""
	def enter(self, player):
		print "\nWhat a terrible work ethic. I'm disappointed. You lose."
		player.playing = False
		exit(1)

# End: You win!
class Win(Scene):
	"""You've gathered enough evidence. You Win."""
	def enter(self, player):
		print "\nYou win"
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

print "You're undercover at a mad scientist's animal-testing lab."
code_name = raw_input("What is your code name? >> ")

a_map = Map("front_door")
a_player = Assistant(code_name)

a_game = Engine(a_map)
a_game.play(a_player)

