from sys import argv

script, input_file = argv

# this function prints the contents of the file to the screen
def print_all(f):
    print f.read()
# the seek() method sets the file's current position at the offset
# SYNTAX: fileObject.seek(offset[, whence])

def rewind(f):
    f.seek(0) # there is no return value

def print_a_line(line_count, f):
    print line_count, f.readline(),

current_file = open(input_file)

print "First let's print the whole file: \n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_file.close()

# NOTES
# The readline() function returns the \n that's in the file at the end of that line.
# Add a comma at the end of the print function calls to avoid adding double \n to every line.
# The seek() function deals in bytes, not lines, and the code seek(0) moves the file to the
# 0 byte in the file.
# current_line is just a variable and has no real connection to the file at all
# Inside readline() is a code that scans each byte of the file until it finds a \n
# character, then stops reading the file to return what it found so far.
# The file f is responsible for maintaining the current position in the file
# after each readlien() call, so that it will keep reading each line.
