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

grand_total = 0
for key in quantities.keys():
    value_each = values[key]
    qty = quantities[key]
    subtotal = value_each * qty
    grand_total += subtotal
print(grand_total / 100)
