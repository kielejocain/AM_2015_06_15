def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
print" Let's do some math with just functions !"

def complex(a, b, c, d):
	print "COMPLEX FUNCTION ( %d - ( %d * ( %d / ( %d ))))" % (a, b, c, d)
	return ( a - ( b * ( c / ( d )))) 
	
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
complex = complex(35, 74, 180, 50) 

print "Age: %d, Height: %d, Weight: %d, IQ: %d, Complex: %d" % (age, height, weight, iq, complex) 

# A puzzle for the extra credit, type it anyway.
print "Here is a puzzle."

# what = add(age, subtract(height, multiply(weight, divide(iq 2))))

# print "That becomes: ", what, "Can you do it by hand?"



