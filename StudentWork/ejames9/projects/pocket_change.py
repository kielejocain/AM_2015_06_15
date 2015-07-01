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


def calc_total():
    total = (quantities[0] * values[0]) + (quantities[1] * values[1]) + (quantities[2] * values[2]) + (quantities[3] * values[3])
    return total

calc_total()
