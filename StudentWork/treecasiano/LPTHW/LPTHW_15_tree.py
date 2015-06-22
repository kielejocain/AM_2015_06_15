from sys import argv

# assigns names to the argvs entered in the command line
script, filename = argv

txt = open(filename) # opens the file

print "Here's your file %r:" % filename
print txt.read() # reads the file, prints to stdout

print "Type the filename again:"
file_again = raw_input('> ')

txt_again = open(file_again)
print txt_again.read()
