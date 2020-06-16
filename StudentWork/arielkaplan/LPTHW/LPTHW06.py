# EXERCISE 06: Strings and Text

# %d is decimal.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# %r is repr --> representation. Passes a string with quotes. 
# Passes a bool as its representation False
print "I said: %r." % x

# %s is string. Passes a string without quotes.
print "I also said: '%s'." % y

# Can store a %r and fill it in later: 
hilarious = False
joke_evaluation = "Isn't that joke so funny? %r"

# This is where the %r is filled in
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
