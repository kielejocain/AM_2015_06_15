
# add a key to the inventory called pocket
# set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'
# .sort() the items in the list stored under the backpack key
# Then .remove('dagger') from the list of items stored under the 'backpack' key.
# Add 50 to the number stored under the 'gold' key.
inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger',  'bedroll', 'bread loaf']
}


inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50
print inventory


# create a new dictionary called prices

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Create a stock dictionary. Loop through each key in prices. For each key, print out the key along with its price and stock information. Print the answer in the following format:
# apple
# price: 2
# stock: 0


stock = {}
stock['banana']=6
stock['apple']=0
stock['orange']=32
stock['pear']=15

for food in prices:
    print food
    print "price: %s" % prices[food]
    print "stock: %s\n" % stock[food]

# Let's determine how much money you would make if you sold all of your food.
# Create a variable called total and set it to zero.
# Loop through the prices dictionaries.For each key in prices,
# multiply the number in prices by the number in stock.
# Print that value into the console and then add it to total.
# Finally, outside your loop, print total.

total = 0

for price in prices:
    money = prices[price] * stock[price]
    print money
    total = total + money

print "The total money is $", total