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

def count_change(vals, quants):
    output = 0.0
    for item in quants.keys():
        print "output is", output
        print "adding value of", quants[item], item, "to the total"
        output += vals[item]*quants[item]*.01
        print "output is now", output
        print "*"*20
    return output

print count_change(values, quantities)