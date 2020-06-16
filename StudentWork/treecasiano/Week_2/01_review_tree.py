## Review of Week 1 concepts

# make a list of three movie titles.

movies = ['Reservoir Dogs', 'Hedwig and the Angry Inch', 'Amelie']

# using a loop and slicing (movies[start:end]), print the first five
# characters and last five characters of each movie title.

for title in movies:
    print "First 5 characters of title: " + title[:5] + "\nLast 5 characters of title: " + title[-5:] + "\n"

# make a dictionary where the keys are fruits and the values are quantities.
# use at least three fruits.

fruits = {'oranges': 5, 'grapefruit': 27, 'cherries': 13}

# define a function that takes two arguments and uses them to update
# the quantity of a fruit.  Please rename the variables to something
# relevant to their meaning.

# def count_update2(fruit, amount):
#     fruits[fruit] += amount

# ALTERNATE VERSION USING KWARGS
def count_update2(inventory, **purchase):
    for item in purchase:
        if item in inventory:
            inventory[item] += purchase[item]
        else:
            inventory[item] = purchase[item]

# Call the function to add 10 to the inventory of your favorite fruit,
# add 5 to the inventory of your second favorite fruit, and subtract
# 10 from the inventory of your least favorite fruit.

# count_update('oranges', 15)
count_update2(fruits, oranges = 5, cherries = 10, grapefruit = -10)

# check to see that it worked!

print fruits
