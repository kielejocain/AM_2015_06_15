## Review of Week 1 concepts

# make a list of three movie titles.

movies = ["Superman", "Batman", "Spider-Man"]

# using a loop and slicing (movies[start:end]), print the first five
# characters and last five characters of each movie title.


print movies



# you could also use a while loop if you like.

for movie in movies:
    print movie[:5]
    print movie[-5:]

# make a dictionary where the keys are fruits and the values are quantities.
# use at least three fruits.

fruits = {"apple": 20, "orange": 15, "peach": 30}

# define a function that takes two arguments and uses them to update
# the quantity of a fruit.  Please rename the variables to something
# relevant to their meaning.

def count_update(number, fruit):
    if fruit in fruits: 
    	fruits[fruit] += number
    else: 
    	fruits[fruit] = number

count_update(10, "peach")
count_update(5, "orange")
count_update(-10, "apple")

# Call the function to add 10 to the inventory of your favorite fruit,
# add 5 to the inventory of your second favorite fruit, and subtract
# 10 from the inventory of your least favorite fruit.



# check to see that it worked!

print fruits