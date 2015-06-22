# Difference of square of sums and sum of squares.

# Find sum of squares of #1-10
sum_of_squares = 0
square_of_sums = 1
total_sum = 0

for i in range(1, 101): 
	square = i * i
	sum_of_squares += square
#	Collect sum of range of #s 
	total_sum += i

square_of_sums = total_sum * total_sum
print sum_of_squares
print square_of_sums

print square_of_sums - sum_of_squares 