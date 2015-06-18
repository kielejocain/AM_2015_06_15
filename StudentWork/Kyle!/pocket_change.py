from sys import argv

script, ones, fives, tens, twentyfives = argv

VALUES = {
    'penny': .01,
    'nickel': .05,
    'dime': .10,
    'quarter': .25
}

pocket = {
    'penny': int(ones),
    'nickel': int(fives),
    'dime': int(tens),
    'quarter': int(twentyfives)
}

value = 0.0

for coin in pocket:
    value += pocket[coin] * VALUES[coin]

print value
