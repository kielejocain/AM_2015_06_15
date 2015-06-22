## Review of Week 1 concepts

# make a list of three movie titles.

movies = ['Jurassic Park', 'Princess Mononoke', 'Mad Max: Fury Road']

# using a loop and slicing (movies[start:end]), print the first five
# characters and last five characters of each movie title.

# you could also use a while loop if you like.

for item in movies:
    print "First five:", item[:5]
    print "Last five:", item[-5:]

# make a dictionary where the keys are fruits and the values are quantities.
# use at least three fruits.

fruits = {'kiwis':10, 'strawberries':30, 'mangoes':5}

# define a function that takes two arguments and uses them to update
# the quantity of a fruit.  Please rename the variables to something
# relevant to their meaning.

def count_update(fruit, number):
    print 'there were', fruits[fruit], fruit
    fruits[fruit] = number 
    print 'now there are', fruits[fruit], fruit
	
# Call the function to add 10 to the inventory of your favorite fruit,
# add 5 to the inventory of your second favorite fruit, and subtract
# 10 from the inventory of your least favorite fruit.

count_update('strawberries', fruits['strawberries'] + 10)
count_update('mangoes', fruits['mangoes'] + 5)
count_update('kiwis', fruits['kiwis'] - 10)

# check to see that it worked!

print fruits
