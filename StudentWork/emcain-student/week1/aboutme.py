my_name = 'Emily Cain'
my_gender = 'f'
my_age = 24
my_weight = 200
my_height = 68
my_eyes = 'green'
my_teeth = 'unfortunate'
my_hair_color = 'brown'
my_hair_texture = 'curly'

my_weight_kg = my_weight * 0.453
my_height_cm = my_height * 2.54
my_height_ft = my_height/12
my_height_rem = my_height%12

def find_pronoun(my_gender):
 if my_gender == 'f':
  return 'she'
 if my_gender == 'm':
  return 'he'
 else:
  return 'they'

my_pronoun = find_pronoun(my_gender)
 

print "Let's talk about %s." % my_name
print "%s is %d years old, weighs %d lbs, and is %d inches tall." % (my_pronoun, my_age, my_weight, my_height)
print "that's the same as %d kilos and 