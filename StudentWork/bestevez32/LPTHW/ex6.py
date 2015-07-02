x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# %s in line 5 is a place holder for lines 2 & 3
y = "Those who know %s and those who %s." % (binary, do_not)

# The next two command lines 8 & 9 will display the previous code
print x
print y

print "I said %r." % x 
print "I also said '%s'." % y 

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e