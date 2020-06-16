# Smallest multiple

# 2520 is the smallest number that can be divided by each 
# of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly 
# divisible by all of the numbers from 1 to 20?

# take dividend
# check if divisible by first num in range 1-10
# if so, check second num
# if not, try next dividend

divisor = 2
max_divisor = 20
dividend = max_divisor

while divisor <= max_divisor:
	if dividend % divisor == 0:
#		print str(dividend) + " is divisible by " + str(divisor)
		divisor += 1
	else:
#		print str(dividend) + " is NOT divisible by " + str(divisor)
		divisor = 2
		dividend += 1
print dividend

