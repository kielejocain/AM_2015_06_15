from random import randint
from sys import exit

class Villain(object):
	def __init__(self, name):
		self.name = name
	
	strength = 10
	
	def attack(self, force):
		print "\"Ouch! That hurt\" %s says." % self.name
		self.strength -= int(force)
		
	def check_strength(self):
		if self.strength <1:
			print "You have slain %s" % self.name
		else:
			print self.name, " has ", self.strength, " life left."
		 
class SuperVillain(Villain):
	strength = 30
	
	def attack(self,force):
		if force >=7:
			print "%s has defended themselves. you only yielded %d damage!" % (
			self.name, (int(force) - 4))
			self.strength -= int(force) -4
		else:
			print "\"Ouch! That hurt!\" %s says." % self.name
			self.strength -= int(force)

green_goblin = Villain("Green Goblin")
loki = SuperVillain("Loki")

class Hero(object):
	life = 20
	force_power = 0
	def __init__(self, name):
		self.name = name
	
	def find_force(self):
		self.force_power += (len(self.name) * randint(3,5))
		return self.force_power
	
	def check_life(self):
		print "You have %d strength left and %d force left" %(
		self.life, self.force_power)
	
		
		

class Scene(object):
	
	def __init__(self):
		pass
		
class Defeated(Scene):
	done = [
	"You failed to recover your possession. You sit in darkness and cry",
	"Not everyone can be a hero. You resolve to hang up your cape forever",
	"You sink into despair and eventual madness without your prized possession",
	"You are inducted into the 'Hero Hall of Disdain'",
	]
	def enter(self):
		print Defeated.done[randint(0, len(self.done)-1)]
		exit(1)
	
	
class Mansion(Scene):
	def enter(self, hero):
		print "Ready to start? Press 'enter' when ready"
		raw_input(">>>")
		print "You're sitting at home, enjoying being an off-duty "
		print "superhero, when your phone buzzes. A text message! You "
		print "glance down, to see an unknown number. "
		print "The message reads: "
		print "I have taken the thing you care for most in the world."
		print "To retrive it, first go to the payphone on the corner. "
		print "DON'T TELL ANYONE!\""
		print "Your heart starts to race, you check the place where you "
		print "hide your valued possession....it's gone!"
		print "Do you: go the the 'payphone' or call your sidekick for 'help'?"
		choice = raw_input(">>> ")
		
		if choice == 'payphone':
			return 'payphone', hero
		
		elif choice == 'help':
			print "What kind of hero calls for help?!?"
			return 'defeated', hero
		
		else:
			print "That's not a choice! Your indecision has cost you greatly"
			return 'defeated', hero
		
class Payphone(Scene):
	def enter(self, hero):
		joker = Villain("The Joker")
		print "Press 'enter' to continue"
		raw_input(">>>  ")
		print "You arrive at the payphone. While you stand in awe that" 
		print "a payphone even exists in this day and age, you see a "
		print "shadowy figure sneak up on your left. "
		print "It's {}!".format(joker.name) 
		print "\"Ha, Ha! You will never find what he has taken!\""
		print "{} says.".format(joker.name)
		print joker.check_strength()
		print "Do you 'attack', 'run away' or 'tell a joke'?"
		choice = raw_input(">>> ")
		
		if choice == 'run away':
			print 'Coward!'
			return 'defeated', hero
		
		elif choice == 'attack':
			while joker.strength > 0:
				print "How much force do you want to use?"
				force = int(raw_input(">>> "))
				print joker.attack(force)
				hero.force_power -= force
				
				if joker.strength % 2 == 0:
					hero.life -= force/2
					print "%s fought back!" % joker.name
				print hero.check_life()
				print joker.check_strength()
			print "Press 'enter' to continue"
			raw_input(">>>   ")
	
			print "Your phone buzzes; another text message from "
			print "the unknown number! It reads: "
			print "'You thought I'd actually use a payphone!? Ha! "
			print "You may have defeated The Joker, but you'll never" 
			print "defeat me. Meet me at dock 17.'"
			print "Press 'enter' to continue"
			raw_input(">>>  ")
			return 'the_docks', hero
		
		elif choice == 'tell a joke':
			print "You sing the only thing you think might get The Joker on your side: "
			print """
		Oh, Jingle Bells, Batman Smells, Robin flew away, 
		Batmobile lost a wheel and the Joker got away, hey.
		Jingle Bells, Batman Smells, Robin flew away,
		Batmobile lost a wheel, oh Happy Christmas Day.
			"""
			effective = randint(1,10)
			if effective <= 5:
				print "'That's not funny! It's not even Christmas' The Joker says"
				return 'defeated', hero
			else:
				print "The Joker can't control his laughter!"
				joker.attack(10)
				print joker.check_strength()
				print "Press 'enter' to continue"
				raw_input(">>>  ")
				print "Your phone buzzes; another text message from the "
				print "unknown number! It reads: "
				print "\"You thought I'd actually use a payphone!? Ha! "
				print "You may have defeated The Joker, but you'll never"
				print "defeat me. Meet me at dock 17...\""
				return 'the_docks', hero
	
class TheDocks(Scene):
	def enter(self, hero):
		print "You race down to the docks, dodging seagulls along the way."
		print "You pass by Dock 15 and see a figure up ahead. It seems "
		print "to be hovering. You come to Dock 16 and the outline "
		print "becomes clear. The Green Goblin is waiting for you. "
		print "You're not sure if he's spotted you yet. "
		
		print "Do you 'attack', try to 'sneak' up on him, or throw "
		print "'bread' at him to attract the seagulls? "

		choice = raw_input(">>> ")
		
		if choice == 'sneak':
			print "You cut around the building, and come to where the"
			print "Green Goblin is, but he's gone! You get the feeling "
			print "that something is watching you. You turn around just "
			print "in time to see the Green Goblin throw a pumpkin bomb!"
			return 'defeated', hero
		
		elif choice == 'attack':
			while green_goblin.strength > 0:
				print "How much force do you want to use?"
				force = int(raw_input(">>> "))
				print green_goblin.attack(force)
				hero.force_power -= force
				print hero.check_life()
				print green_goblin.check_strength()
			print "Press 'enter' to continue"
			raw_input(">>>   ")
			return 'abandoned_warehouse', hero
		
		elif choice == 'bread':
			print "You grab the stale bowl of bread convienently sitting"
			print "on a pile of pallets and throw handfuls towards the "
			print "Green Goblin. The seagulls swarm the villain and his "
			print "cape gets twisted up; he loses his balance and falls"
			print "from the hoverboard."
			print green_goblin.attack(10)
			print green_goblin.check_strength()
			print"Press 'enter' to continue"
			raw_input(">>>  ")
			return 'abandoned_warehouse', hero
	

class AbandonedWarehouse(Scene):
	def enter(self, hero):
		print "With the Green Goblin safely out of the way, you race "
		print "into the	warehouse. It appears to be abandoned, naturally."
		print "Swooping down from a crane is Loki. You realize you're in"
		print "for the fight of your life. You hope you have enough "
		print "strength left..."
		print loki.check_strength()
		print hero.check_life()
		while (loki.strength >= 1) and ((hero.life >= 1) and (hero.force_power >= 1)) :
			print loki.check_strength()
			print hero.check_life()
			print "How much force do you want to use?"
			force = int(raw_input(">>> "))
			loki.attack(force)
			hero.force_power -= int(force)
		if loki.strength < 1 and hero.life > 1:
			print """
You have defeated Loki! Congratulations! You are able to recover your 
most prized posession: a grilled cheese sandwich which you then eat.
			"""
			return exit(1)
		else:
			print "Loki is too powerful for you!"
			return 'defeated', hero

class Finished(Scene):
	pass	

class Engine(object):
	scenes = {
		'mansion': Mansion(),
		'payphone': Payphone(),
		'the_docks': TheDocks(),
		'abandoned_warehouse': AbandonedWarehouse(),
		'defeated': Defeated(),
		'finished': Finished()
	} 
		
	def play(self):
		print "Welome to my game! What's your superhero name?"
		hero_name = raw_input(">>>  ")
		hero = Hero(hero_name)
		hero.find_force()
		
		print hero.check_life()
		
		current_scene = self.scenes['mansion']
		last_scene = self.scenes['finished']
		
		while current_scene != last_scene:
			next_scene_name, hero = current_scene.enter(hero)
			current_scene = self.scenes[next_scene_name]
			
		current_scene.enter()


a_game = Engine()
a_game.play()
