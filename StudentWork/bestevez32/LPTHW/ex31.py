print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input(">")

if door == "1":
	print "There is a giant bugbear protecting a box that emanates a magical aura."
	print "1. Use your magic ring to become invisible and try to steal the box."
	print "2. Fight the bugbear and take the box."
	
	bugbear = raw_input(">")
	
	if bugbear == "1":
		print "You manage to grasp the box but not before the bear smells you and eats your arm off! You slowly bleed out and die."
	elif bugbear == "2":
		print "You put up a valiant fight but succumb to wounds. The bugbear eventually gnaws your face off."
	else:
		print "Well, doing %s is probably better. Bugbear runs away." % bugbear
		
elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow, jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input(">")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good Job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good Job!"
else:
	print "You stumble around and fall on a knife and die. Good Job!"
		
		
	
