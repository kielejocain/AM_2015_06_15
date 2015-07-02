## Review of Week 1 concepts

# make a list of three movie titles.

movies = ['Terminator', 'The Avengers', 'The Princess Bride']

# using a loop and slicing (movies[start:end]), print the first five
# characters and last five characters of each movie title.

movies[0:6]
movies[-6:-1]

print movies

# you could also use a while loop if you like.

for movie in movies:
	print movie[:5]
	print movie[-5:]

#for thing in list:
    #pass

# make a dictionary where the keys are fruits and the values are quantities.
# use at least three fruits.

fruits = {'oranges': 5, 'peaches': 10, 'mangos' : 1
}

# define a function that takes two arguments and uses them to update
# the quantity of a fruit.  Please rename the variables to something
# relevant to their meaning.

def count_update(total, fruit):

	if fruit in fruits:
		fruits[fruit] += total
	else:
		fruits[fruit] = total 
   

# Call the function to add 10 to the inventory of your favorite fruit,
# add 5 to the inventory of your second favorite fruit, and subtract
# 10 from the inventory of your least favorite fruit.
	
count_update(10, 'mangos')
count_update(5, 'oranges')
count_update(-10, 'peaches')



# check to see that it worked!

print fruits
