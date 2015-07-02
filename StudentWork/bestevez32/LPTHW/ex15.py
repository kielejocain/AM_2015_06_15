from sys import argv # argument vector
# Lines 1 -3 uses argv (argument vector) to get filename.
script, filename = argv #(argument vector)
# Line 5 opens the particular file by its name.
txt = open(filename)

print "Here's you file %r:" % filename # Line 7 & 8 prints
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()

