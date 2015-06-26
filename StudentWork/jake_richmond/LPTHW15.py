from sys import argv # argv == Argument Vector
# Lines 1 and 3 open up filename
script, filename = argv
# line 5 opens the file name you entered
txt = open(filename)
# this prints your file name and the text in the file
print "Here's your file %r:" % filename
print txt.read()
# here it asks you to type the file name again and then opens the file that you input
print "Type the filename again:"
file_again = raw_input("> ")
# Here it opens the file you entered and prints it out for you
txt_again = open(file_again)

print txt_again.read()