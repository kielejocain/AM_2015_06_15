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
    total = (quantities["pennies"] * values["pennies"]) + (quantities["nickels"] * values["nickels"]) + (quantities["dimes"] * values["dimes"]) + (quantities["quarters"] * values["quarters"])
    print "$%f"   % (total / 100.0)

calc_total()





# TODO calculate total dollar amount