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
penny_cents = values["pennies"] * quantities["pennies"]
nickel_cents = values["nickels"] * quantities["nickels"]
dime_cents = values["dimes"] * quantities["dimes"]
quarter_cents = values["quarters"] * quantities["quarters"]
totals_list = [penny_cents, nickel_cents, dime_cents, quarter_cents]
total_cents = sum(totals_list)
dollar_amount = float(total_cents) / 100

print quantities["pennies"], "pennies, worth", penny_cents, "cents."
print quantities["nickels"], "nickels, worth", nickel_cents, "cents."
print quantities["dimes"], "dimes, worth", dime_cents, "cents."
print quantities["quarters"], "quarters, worth", quarter_cents, "cents."
print "cents:", total_cents
print "dollar amount:", dollar_amount