# Even Fibonacci numbers

# Each new term in the Fibonacci sequence is generated by adding the 
# previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values 
# do not exceed four million, find the sum of the even-valued terms.

fib = [1, 2]
max_of_sequence = 4000000

# Add last two numbers and append the sum to the end of the list.
while fib[-1] + fib[-2] <= max_of_sequence :
	fib.append( fib[-1] + fib[-2])
print "\nFibonacci sequence ending at " + str(max_of_sequence) + ":"
print fib

total = 0
i = 0

# If number is even, add it to total.
while i < len(fib) :
	if fib[i] % 2 == 0 :
		# print fib[i]
		total += fib[i]
	i += 1
print "\nTotal of even values in above sequence:"
print total