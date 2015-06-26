## Review of Week 1 concepts

# make a list of three movie titles.

movies = ["Finding_Nemo", "Beauty_and_the_Beast", "The_Little_Mermaid"]

# using a loop and slicing (movies[start:end]), print the first five
# characters and last five characters of each movie title.

# you could also use a while loop if you like.

for i in movies:
	print (i[:5] + i[-5:])
    

# make a dictionary where the keys are fruits and the values are quantities.
# use at least three fruits.

fruits = {"apple": 2, "kiwi": 5, "banana": 30}

# define a function that takes two arguments and uses them to update
# the quantity of a fruit.  Please rename the variables to something
# relevant to their meaning.
print fruits

def count_update(food, quantity):
	for key in fruits:
		if key == food:
			fruits[food] += quantity
		else:
			pass
		
    

# Call the function to add 10 to the inventory of your favorite fruit,
# add 5 to the inventory of your second favorite fruit, and subtract
# 10 from the inventory of your least favorite fruit.

count_update("kiwi", 10)
count_update("apple", 5)
count_update("banana", -10)

# check to see that it worked!

print fruits
