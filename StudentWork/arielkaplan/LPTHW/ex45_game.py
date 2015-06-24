from sys import exit
from random import random, randint

keep_playing = True
health = 100
evidence = 0
carrying = []

# ENGINE
class Engine(object):
	"""Runs game"""


	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		# Starting scene of the game
		current_scene = self.scene_map.opening_scene()
		
		# needs loop or won't change rooms more than once
		while keep_playing == True: 
			# uses returned value for next chosen scene from current scene.enter()
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

		# runs new scene
		current_scene.enter()

# PLAYER

# Don't actually think I need this. Made variables global for ease of modification
# class Assistant(object):
# 	"""Player is an undercover lab assistant. Resuce animals
# 	and collect evidence without getting caught or too injured."""
# 	def __init__(self):
# 		self.health = 100
# 		self.evidence = 0
# 		self.carrying = {} # animals


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
		self.value = 3

	def __repr__(self):
		return ("Bunny\n\tTeeth: " + str(self.teeth) + 
			    "\n\tClaws: " + str(self.claws) +
			    "\n\tValue: " + str(self.value))


class Cat(Animal):
	"""Mediumest of animals."""
	def __init__(self, danger):
		super(Cat, self).__init__()
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
	global keep_playing
	global health
	global evidence
	global carrying

	def enter(self):
		print "Not yet configured."
		exit(1)
		
# Entry door
class FrontDoor(Scene):
	"""Figure the combination code to get in the lab."""
	def enter(self):
		print "\nYou're at the front door. Yay."
		print "I'm gonna assume you got the code right. Lucky you."
		return "hallway"

# Hallway
class Hallway(Scene):
	"""Lets player choose lab room"""
	def enter(self):
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
			self.enter()

# Labs: make four instances
class Lab(Scene):
	"""docstring for Lab"""
	def __init__(self, color, cages):
		self.color = color
		self.cages = cages
		if self.cages == []:
			self.fill_cages()

	def enter(self):
		print "\nYou've made it to the %s Room." % self.color
		print "There are %d occupied cages." % len(self.cages)

		self.pick_up_animals()

		return "hallway"

	def fill_cages(self):
		"""Random 4-8 cages"""

		# arguments currently don't mean anything
		species = [Bunny(1), Cat(2), Dog(3)]

		# between 4 and 8 cages
		for i in range(randint(4,8)):
			# creates a random animal in each cage
			self.cages.append(species[randint(0, 2)])

	def pick_up_animals(self):
		print "\nWhich animals to rescue?"
		for i in range(len(self.cages)):
			# hiding stats for now
			print str(i + 1) + ": " + str(self.cages[i])
		print str(len(self.cages) + 1) + ": None"
		
		pick_up = raw_input("Which animal do you pick up? >> ")

		# check that pick_up is a number

		pick_up = int(pick_up)
		# switch from cardinal to ordinal #
		pick_up -= 1

		# add animal to pack & remove from cage
		if self.cages[pick_up] == "Empty Cage":
			print "You already got that one. Pick something else."
			self.pick_up_animals()
		elif 0 <= pick_up <= len(self.cages):
			carrying.append(self.cages[pick_up])
			print carrying
			self.cages[pick_up] = "Empty Cage"


		elif pick_up == len(self.cages + 1):
			return self.leave()
		else:
			print "You seem confused. You're worrying me."
			self.enter()


	def leave(self):
		print "Okay, let's go."
		return "hallway"

class Drop(Scene):
	"""Drop off animals carrying outside"""
	def enter(self):
		# pull amt of evidence out of carrying dict.
		print "\nYou put the animals in a safe place."
		print "You've collected ??? of the evidence you need." 
		if evidence >= 100:
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
	def enter(self):
		print "You got caught"
		pass

# End: Pass out
class PassOut(Scene):
	"""Health has reached 0. Game Over."""
	def enter(self):
		print "\nA valiant effort, but the animals did too much damage to you."
		print "You pass out in the lab and are found the next morning."
		print "The mad scientist fires you for sleeping on the job."
		keep_playing = False
		exit(1)

# End: Give up
class GiveUp(Scene):
	"""You got bored and gave up."""
	def enter(self):
		print "\nWhat a terrible work ethic. I'm disappointed. You lose."
		keep_playing = False
		exit(1)

# End: You win!
class Win(Scene):
	"""You've gathered enough evidence. You Win."""
	def enter(self):
		print "\nYou win"
		keep_playing = False
		# exit(1)

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



a_map = Map("front_door")

a_game = Engine(a_map)
a_game.play()

