from sys import argv

script, filename = argv #get the file name using argv

txt = open(filename) #opens a file based on what you input in argv, returns a file object called txt

print "Here's you file %r: " % filename #displays the name of the file as you entered it with argv
print txt.read() #calls "read" on the object "txt", which returns a string generated from the file. 

#note: you don't do read again on the same file object because the cursor will be at the end and it will return an empty string. You can reset the cursor, or make a new file object as below. 

print "Type the filename again:"
file_again = raw_input("> ") #asks for the file name with raw_input

txt_again = open(file_again) #as above, opens the file and creates a file object called txt_again

print txt_again.read() #prints the string etc.

#other useful commands: echo to append stuff to text files, create text files ; seek(0) to return to first byte of file. 