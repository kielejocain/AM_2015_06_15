# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this one just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."

print_two("Kyle", "Joecken")
print_two_again("Kevin", "Bacon")
print_one("abracadabra")
print_none()

# *args exists as a list of arguments, which can be unpacked and used in the
# function code

# **kwargs is also useful, but instead of a list the arguments are stored
# as a dictionary.
