from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print "Copying from %s to %s" % (from_file, to_file)

# We could do these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()

# making it shorter...
indata = open(from_file).read()

# print "The input file is %d bytes long" % len(indata)

# print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()

# out_file = open(to_file, "w")
# out_file.write(indata)

# this one shorter too.
out_file = open(to_file, "w").write(indata)

print "Copied from %s to %s" % (from_file, to_file)

# Don't need to close file; should be automatically closed.
# "You probably did something like this, indata = open(from_file).read(), 
# which means you don't need to then do in_file.close() when you reach 
# the end of the script. It should already be closed by Python once 
# that one line runs." 
# out_file.close()
# in_file.close()