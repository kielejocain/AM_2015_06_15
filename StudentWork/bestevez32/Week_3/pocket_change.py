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
# define a function: (amount_in_dollar) that takes a variable: (denomination)
def amount_in_dollar(denomination):
    # This line takes the values and quantities and multiplies them.
    total_dollar = values[denomination] * quantities[denomination]
    # return float allows for 2.001 of the total dollar amount divided by 100.
    return float(total_dollar)/100
# The print function adds all amounts and dicplays the total.
print amount_in_dollar("pennies") + amount_in_dollar("nickels") + amount_in_dollar("dimes") + amount_in_dollar("quarters")
