from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL_C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# we pass in the 'w' for "write mode" which truncates the file
# if it already exists
target = open(filename, 'w')

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write('%s\n%s\n%s\n' % (line1, line2, line3))

print ('And finally, we close it.')
target.close()
