#define the string x and format with 10 as the decimal inside
x = "There are %d types of people." % 10

#define the string binary to contain "binary"
binary = "binary"
#define the string do_not to contain "don't"
do_not = "don't"
#define the string y to the joke's punchline, inserting the strings binary and do_not
#STRING IN STRING
y = "Those who know %s and those who %s." % (binary, do_not)

#print the two lines of the joke
print x
print y

#quote the two lines of the joke, first using a repr and then using a string format.
#STRING IN STRING
 
print "I said: %r." % x

STRING IN STRING

print "I also said: '%s'." % y

#define the boolean hilarious to contain False
hilarious = False
#define the string joke_evaluation, with a spot for a variable to be inserted that has not yet been defined
joke_evaluation = "Isn't that joke so funny?! %r"

#convert the boolean hilarious into a string and insert it into joke_evaluation
#STRING IN STRING

print joke_evaluation % hilarious

#define the strings w and e
w = "This is the left side of..."
e = "a string with a right side."

# concatenate w and e and print the resulting string.
print w + e


    # Go through this program and write a comment above each line explaining it.
    # Find all the places where a string is put inside a string. There are four places.
    # Are you sure there are only four places? How do you know? Maybe I like lying.
    # Explain why adding the two strings w and e with + makes a longer string.
