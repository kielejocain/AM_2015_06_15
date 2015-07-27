__author__ = 'Emily'


inp_no = int(raw_input("Please enter a positive integer:  "))

output = 1
i = 2

while i <= inp_no:
    output *= i
    i += 1

print output
