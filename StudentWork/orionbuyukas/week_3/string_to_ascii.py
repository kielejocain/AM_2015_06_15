
print "welcome to string converter\n" + "=" *20 + "+" * 20
string = raw_input("Enter a string to convert:  ")

def string_to_ascii(string):
    output = []
    for c in string:
        letter = ord(c)
        print letter
        print bin(letter)
        output.append(letter)
    return output
