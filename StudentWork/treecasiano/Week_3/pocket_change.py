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

def total(coin):
    cents = values[coin] * quantities[coin]
    return float(cents)/100



print "$%.2f" % total("pennies")
print "$%.2f" % total("nickels")
print "$%.2f" % total("dimes")
print "$%.2f" % total("quarters")