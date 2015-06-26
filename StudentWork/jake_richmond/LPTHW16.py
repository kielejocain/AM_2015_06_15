from sys import argv
# Defining script and filename
script, filename = argv
# Printing instructions on what to do
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")
# Defines and opens the target name in write format
print "Opening the file..."
target = open(filename, 'w')
# Emptys out the file
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I am going to ask you for three lines."
# asks you for three new lines and inputs the three new lines into your file
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()