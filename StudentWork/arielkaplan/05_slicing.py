# Using the given string, here are a few string slicing exercises to attempt.
# string[start:end] or string[start:end:step]

s = "Hello world"

# Exercise 1: I want to live in a Jello world.  Do it with slicing.

t = "J" + s[1:]
print t

# Exercise 2: Use stepping to get the string 'lowrd'.

u = s[2::2]
print u

# Exercise 3: Use a negative step to print 'row'.  Hint: try s[::-1]

v = s[8:5:-1]
print v


w = s[4::-1] 
# olleH. ** make ending index blank to get it to go to the end.
# end index -1 won't print. end index 0 doesn't give the H.
print w