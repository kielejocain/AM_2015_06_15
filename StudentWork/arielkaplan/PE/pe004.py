# largest palindrome product

# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of 
# two 2-digit numbers is 9009 = 91 x 99. 
# Find the largest palindrome made from the product of 
# two 3-digit numbers.

# specify highest starting numbers
# keep first the same and subtract one from the second
# check if product is palindrome
# repeat, with first number less 1.
# (Loop w/in loop)

# how to check if palindrome:
# while length > 1? 
# 	continue while number[first] == number [last]
# 		pop first and last numbers

def is_palindrome(number):
	"""Takes a number. Returns boolean."""
	
	# Takin' the long way around....
	# digits = []
	# number = str(number)

	# for d in number:
	# 	digits.append(d)

	# while (len(digits) >= 2) and (digits[0] == digits[-1]): 
	# 	digits.pop(0)
	# 	digits.pop(-1)

	# if len(digits) <= 1:
	# 	return True
	# else:
	# 	return False

	number = str(number)
	rebmun = number[::-1]
	if number == rebmun:
		return True
	else:
		return False

palindromes = []

# loops backwards
for i in range(999, 99, -1):
	for j in range(999, 99, -1):
		if is_palindrome(i * j):
			palindromes.append(i * j)
			print str(i) + " * " + str(j) + " = " + str(i * j)

print max(palindromes)


# is_palindrome(6)
# is_palindrome(33)
# is_palindrome(555)
# is_palindrome(9009)
# is_palindrome(636)

# is_palindrome(50)
# is_palindrome(5553)
# is_palindrome(3563)
# is_palindrome(932)

