from sys import exit
from random import randint

class Hero(object):
	def __init__(self):
		self.name = raw_input("What is your name?")
		self.spells = 3 
		self.healing_potion = 2
		self.hit_points = 10 
		self.wound = {
			'attack' : "Its weapon bites deep into your flesh.",
			'spell' : "You scream!."
			}
		self.death = {
			'attack' : "You scream out in a blood curdling shriek!"
			}
	
	def drink(self):
		self.healing_potion -= 1
		self.hit_points += 5
		print("You knock back a potion and suddenly feel invigorated.")
		print("You now have " + (str(self.hit_points)) +" hit points.")
		print("You now have " + (str(self.healing_potion)) + " potions" ) 
	
	def attack(self, other):
		x = randint(0,3)
		if x > 0:
			print("\nYour attack is successful and hits for %d damage.") % x 
		else:
			print("Your attack misses the enemy.")
		other.life -= x 
		other.get_hit('attack') 
			
	def cast(self, other):
		self.spells -= 1
		other.life -= 3
		other.get_hit('spell')
		if self.spells >= 0:
			print "\nYou have " + (str(self.spells) + " spells left.")
		else:
			self.hit_points -=2
			print "\nYou have run out of magical energy and must tap into your life force."
			print "This will allow you to cast another spell at the cost of 2 hit points."
			print "\nYou have " + (str(self.hit_points) + " hit points left.")

	def get_hit(self, attack):
		if self.hit_points > 0:
			print self.wound[attack]
			print "\n%s you have %d hit points left." % (self.name, self.hit_points) 
		
class Enemy(object):
	
	def __init__(self, life):
		self.life = life
		self.wound = {
			'attack': "\nThe enemy spits out a mouth full of teeth, and prepares to take a swing at you.",
			'spell': "The enemy shrieks in pain!"
		}
		self.death = {
			'attack' : "Your enemy falls, its lifeless body crumples to the ground.",
			'spell' : "\nA wave of magical energy emanates from your fingertips."
		}
	
	def attack(self, hero):
		print("\nThe enemy attacks you!")
		hero.hit_points -= 1 
		hero.get_hit('attack')
		
		if self.life <=0:
			print self.death['attack'] 
			return False
		else: 
			return True 
		
		if hero.hit_points <=0:
			print hero.death['attack'] 
			return False
		else:
			return True
		
	def spell(self):
		print("A wave of magical energy emanates from your finger tips.")
		self.life -=3
		if self.life <=0:
			print("Where an enemy once stood, now all that remains is a smouldering corpse.")
		else:
			print"It has "+ (str(self.life) + "life left.") 
			
	def get_hit(self, attack):
		if self.life > 0:
			print self.wound[attack]
			print "It has %d hit points left." % self.life
		else:
			print self.death[attack]
			
			
			
			 
class Scene(object):

	def enter(self):
		print "This scene is not yet configured."
		
		exit(1) 
		
class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished') 
		my_hero = Hero() 
		
		while current_scene != last_scene:
			next_scene_name, my_hero = current_scene.enter(my_hero) 
			current_scene = self.scene_map.next_scene(next_scene_name)
		
		current_scene.enter()		
		
class Death(Scene):

	quips = [
		"You died a horrible death that can only be explained as inconceivable.",
		"Your mostly dead body is dragged down to the Pit of Despair.",
		"In the very near future a goblin will use your skull as a drinking mug!",
		"You need a miracle Max, in case you didn't notice... Your dead!"
	]

	def enter(self, hero):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)
		

class TownSquare(Scene):
	
	def enter(self, hero):
	
		print """\n%r you have been hired by a local trade guild to ensure that 
a shipment of goods safely arrives in time for the annual swallow-tail 
festival. Much to your dismay %r you discover that the bustling town of 
Sand Point has been invaded by an army of goblins hell-bent on running amok. 
They carry weapons that appear to be fashioned from jagged hunks of rusty 
metal. There shrill voices quieted only by the screams of the towns villagers. 
A group of three goblins fix their beady eyes in your general direction.
%r what do you do?""" % (hero.name, hero.name, hero.name) 
		enemy1 = Enemy(3)
		
		while enemy1.life > 0:
			action = raw_input("> ")
			if action == "attack":
				hero.attack(enemy1)
				alive = enemy1.attack(hero) # no need to define alive 
				if not alive:               # will return True or False 
					return 'death', hero
				continue 
			
			elif action == "spell":
				hero.cast(enemy1) 
				continue
				
			elif action == "potion":
				hero.drink() 
				continue
				
			else:
				print "What?"
				continue
			
		return 'waterworks', hero

class Waterworks(Scene):

	def enter(self, hero):
		
		print """\n%r your victory celebration is short lived. Just east of the 
town square you see the waterworks and a group of enemies gathering in 
front of it. They are carrying torches and it appears they are determined  
to light it on fire. The waterworks is an integral part of the economy of 
Sand Point, and without it, the long term suffering of its town folk would be 
unthinkable. As you approach the building you hear a deep voice cry out from 
behind you, "What do we have here!" You draw your sword and spin on your heals. 
A monster the size of a bear stares you down with a menacing gaze. 
It smells as though it has bathed in the blood of a corpse, and its 
large talons and beak can only mean one thing. %r you are about to 
square off against a Bugbear and this combat will prove to be more difficult
than your last encounter. 
%r What do you do?""" % (hero.name, hero.name, hero.name) 
		Bugbear = Enemy(15)
		
		while Bugbear.life > 0:
			action = raw_input("> ")
			if action == "attack":
				hero.attack(Bugbear)
				alive = Bugbear.attack(hero) 
				if not alive:     
					return 'death', hero
				continue 
			
			elif action == "spell":
				hero.cast(Bugbear) 
				continue
				
			else:
				print "What?"
				continue

		return 'finished', hero
		
class Finished(Scene):
	
	def enter(self):
		print "You won!"
		exit(0)
		
class Map(object):

	scenes = {
		'town_square' : TownSquare(),
		'waterworks' : Waterworks(),
		'death' : Death(),
		'finished': Finished()
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('town_square') 
a_game = Engine(a_map)
a_game.play()