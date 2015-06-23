from sys import exit
from random import randint


name = raw_input("What is your name?")
print "\nWelcome %s." % name

# figure out how to use these attributes as a method.  

spells = int(3) 
print "You now have %d spells." % spells 

healing_potions = int(2) 
print "You now have %d healing potions." % healing_potions 

hit_points = int(10)
print "You now have %d hit points." % hit_points 

pass 


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
		
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
		
		current_scene.enter()		
		
class Death(Scene):

	quips = [
		"You died a horrible death that can only be explained as inconceivable.",
		"Your mostly dead body is dragged down to the Pit of Despair.",
		"In the very near future a goblin will use your skull as a drinking mug!",
		"You need a miracle Max, in case you didn't notice... Your dead!"
	]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)
		

class TownSquare(Scene):
	
	def enter(self):
	
		print """\n%r you have been hired by a local trade guild to ensure that a
shipment of goods safely arrives in time for the annual swallow-tail festival.
Much to your dismay %r you discover that the bustling town of Sand Point 
has been invaded by an army of goblins hell-bent on running amok. They carry
weapons that appear to be fashioned from jagged hunks of rusty metal. There 
shrill voices quieted only by the screaming coming from the towns villagers. A 
group of three goblins fix their beady eyes in your general direction.
%r what do you do?""" % (name, name, name) 
		
		action = raw_input("> ")
		
		if action == "attack":
			print "The goblin horde overtakes you."
			return 'death' 
			
		elif action == "spell":
			print """\nA wave of magical energy emanates from your finger tips, the goblin horde is 
engulfed in flames."""
			print "You now have %d spells." % spells  
			return 'death'

class Finished(Scene):
	
	def enter(self):
		print "You won!"
		return 'finished'
		
class Map(object):

	scenes = {
		'town_square' : TownSquare(),
		'death' : Death()
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