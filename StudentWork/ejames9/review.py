## Review of Week 1 concepts

# make a list of three movie titles.

movies = ["The Wall", "Finding Nemo", "Bittersweet Motel"]
for mov in movies:
    print mov[:6] + mov[-5:]

# using a loop and slicing (movies[start:end]), print the first five
# characters and last five characters of each movie title.

# you could also use a while loop if you like.



# make a dictionary where the keys are fruits and the values are quantities.
# use at least three fruits.

fruits = {"Apples": 1, "Oranges": 2, "Pears": 3}



# define a function that takes two arguments and uses them to update
# the quantity of a fruit.  Please rename the variables to something
# relevant to their meaning.

def count_update(fruit, num):
    if fruit in fruits:
        fruits[fruit] += num
        print fruits
    else:
        fruits[fruit] = num
        print fruits


# Call the function to add 10 to the inventory of your favorite fruit,
# add 5 to the inventory of your second favorite fruit, and subtract
# 10 from the inventory of your least favorite fruit.


count_update("Apples", 10)
count_update("Oranges", 5)
count_update("Pears", -10)
