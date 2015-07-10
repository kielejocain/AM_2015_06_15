## Review of Week 1 concepts

# make a list of three movie titles.

movies = ['Avatar', 'The Imitation Game', 'Bruce Almighty']

# using a loop and slicing (movies[start:end]), print the first five
# characters and last five characters of each movie title.
for movie in movies:
    print movie[:5]
# you could also use a while loop if you like.

# make a dictionary where the keys are fruits and the values are quantities.
# use at least three fruits.

fruits = {'bananas': 4, 'apples': 10, 'oranges': 1}

# define a function that takes two arguments and uses them to update
# the quantity of a fruit.  Please rename the variables to something
# relevant to their meaning.

def count_update(key, value):
    fruits[key] = fruits.get(key, 0) + value

# Call the function to add 10 to the inventory of your favorite fruit,
# add 5 to the inventory of your second favorite fruit, and subtract
# 10 from the inventory of your least favorite fruit.
count_update('apples', 10)
count_update('bananas', 5)
count_update('oranges', -10)


# check to see that it worked!

print fruits
