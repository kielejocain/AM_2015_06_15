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
def find_total(values, quantities):
    total = 0
    # loop through value dict and find key
    for key in values:
        value_key = values[key]
        # find matching key in quantity dict
        if key in quantities:
            # multiply value and quantity
            quantity_key = quantities[key]
            # add to total
            total += (value_key * quantity_key)
    return total


print find_total(values, quantities)
