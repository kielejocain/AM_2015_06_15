# These exercises are from http://erlerobotics.gitbooks.io/erle-robotics-learning-python-gitbook-free/content/lists/exercises_list_and_dictionaries.html

# add a key to the inventory called pocket
# set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'
# .sort() the items in the list stored under the backpack key
# Then .remove('dagger') from the list of items stored under the 'backpack' key.
# Add 50 to the number stored under the 'gold' key.
inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}


# create a new dictionary called prices

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Loop through each key in prices. For each key, print out the key along with its price and stock information. Print the answer in the following format:
# apple
# price: 2
# stock: 0








# Let's determine how much money you would make if you sold all of your food.
# Create a variable called total and set it to zero.
# Loop through the prices dictionaries.For each key in prices,
# multiply the number in prices by the number in stock.
# Print that value into the console and then add it to total.
# Finally, outside your loop, print total.