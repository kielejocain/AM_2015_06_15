__author__ = 'Emily'

def factorial(n, output=None):
    if output is None:
        output = 1
        print "setting output to 1"
    if n == 1:
        print output, "is the answer"
        return output
    funct = output
    funct*= n
    print "multiplying funct", funct, "by n", n

    print "calling factorial(", n-1, funct, ")"
    factorial(n-1, funct)




inp_no = int(raw_input("Please enter a positive integer:  "))

item = factorial(inp_no)

print item