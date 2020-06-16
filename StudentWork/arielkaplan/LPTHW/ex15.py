# EXERCISE 15: Reading Files

# from system (when file is run), import some arguments
from sys import argv

# Two arguments, named script and filename
script, filename = argv

# txt is variable representation for text file
# open returns a file object, the file that we entered as our
# second argument
txt = open(filename)

# Tells us which file we opened
print "Here's your file %r" % filename
# Prints the contents of our opened text file
# Cursor will be at the end of the file once this is done
print txt.read()

print "Type the filename again:"
# takes the filename and stores it in file_again
file_again = raw_input("> ")

# opens the same file and saves it into txt_again
txt_again = open(file_again)

# prints the opened file that was saved in txt_again
print txt_again.read()

# close files to prevent memory leakage
txt.close()
txt_again.close()
