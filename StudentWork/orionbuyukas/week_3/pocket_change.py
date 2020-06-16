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

def pocket_calculator(values, quantities):
    total = 0.00
    for key in values.keys():
        total += (values[key] * quantities[key])/100.00
    print "$" + total
