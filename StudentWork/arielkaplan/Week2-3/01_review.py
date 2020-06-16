## Review of Week 1 concepts

# make a list of three movie titles.

movies = ["Lord of the Rings", "Spirited Away", "Amelie"]

# using a loop and slicing (movies[start:end]), print the first five
# characters and last five characters of each movie title.

# you could also use a while loop if you like.

for movie in movies:
    print movie[:5] + movie[-5:]

# make a dictionary where the keys are fruits and the values are quantities.
# use at least three fruits.

fruits = {"pineapple": 3, "strawberry": 200, "watermelon": 4, "banana": 15}

# define a function that takes two arguments and uses them to update
# the quantity of a fruit.  Please rename the variables to something
# relevant to their meaning.

def count_update(fruit, quantity):
    """Add quantity to current inventory"""
    if fruit in fruits:
	    fruits[fruit] += quantity
	else:
		fruits[fruit] = quantity

# Call the function to add 10 to the inventory of your favorite fruit,
# add 5 to the inventory of your second favorite fruit, and subtract
# 10 from the inventory of your least favorite fruit.

count_update("strawberry", 10)
count_update("watermelon", 5)
count_update("banana", -10)

# check to see that it worked!

print fruits
