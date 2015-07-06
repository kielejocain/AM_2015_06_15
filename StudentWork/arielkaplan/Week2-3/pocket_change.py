values = {
    "pennies": 1,
    "nickels": 5,
    "dimes": 10,
    "quarters": 25
}

quantities = {
    "pennies": 13,
    "nickels": 3,
    "dimes": 2,
    "quarters": 4
}

# TODO calculate total dollar amount

change = {}
for key in values:
    change[key] = []
    change[key].append(values[key])
for key in quantities:
    change[key].append(quantities[key])

print change

def calculate_change(change):
    total = 0
    for coin in change:
        value = change[coin][0]
        how_many = change[coin][1]
        total += (value * how_many)
    # convert from cents to dollars
    total /= 100.0
    return total

print calculate_change(change)