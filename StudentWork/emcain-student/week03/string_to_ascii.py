__author__ = 'Emily'

the_chr= raw_input("please enter a single character >> ")
print "this is your character rendered as a number: ", ord(the_chr)
print " \o/ <yay! "
the_number = raw_input("please enter a number between 0 and 225 (inclusive) >> ")
print "this is your number rendered as a character: ", chr(int(the_number))
print "cool, now let's do it for a string"
the_str = raw_input("please enter any amount of text >> ")
print "here are the numbers used to represent the characters in your string."
i = 0
for c in the_str:
    print "Character", i, ",", c, "is represented by the number", ord(c)
    i += 1
print "thanks for playing!"
