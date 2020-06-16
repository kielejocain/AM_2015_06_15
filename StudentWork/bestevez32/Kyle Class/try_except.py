## ValueError

print "Raise a ValueError by entering something other than an integer."
error = False
while not error:
    try:
        print 7 + int(raw_input("What number should I add to 7? > "))
    except ValueError:
        print "That's no integer..."
        error = True

# IndexError, KeyError

fruits = ["apples", "bananas", "oranges"]
print "Raise an IndexError by entering an integer other than 0, 1, or 2."
error = False
while not error:
    try:
        print fruits[int(raw_input("Which of my fruits would you like? (0/1/2)> "))]
    except IndexError:
        print "I don't have a fruit by that number."
        error = True
    except ValueError:
        print "We've already played with ValueErrors!"

# ZeroDivisionError

print "Raise a ZeroDivisionError by entering 0."
error = False
while not error:
    try:
        print "You have 20 cookies.  How many friends do you have?"
        print "Each friend gets %d cookies." % (20.0 / int(raw_input("> ")))
    except ZeroDivisionError:
        print "No one has 0 friends."
        error = True
    except ValueError:
        print "Stop with the ValueErrors already!"

# TypeError

print "Finally, I'll raise a TypeError by adding a string and an integer."
print "I won't make a custom error handling, so the script will fail and end."
raw_input("Ready? ")
print "cheese" + 2
