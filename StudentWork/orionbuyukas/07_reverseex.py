# this script should take in a sentence or statement from the user,
# then repeat that statement back with the words in reverse order.
# Do not reverse the words themselves!


statement = raw_input("Please enter a staetment to reverse.\n>> ")
min = 0
max = 0
words = []

for i in range(len(statement)): #i is the index letter we're checking
    if statement[i] == ' ': #creates a list of integers
        max = i
        words.append(statement[min:max])
        min = max + 1

words.append(statement[min:])

sdrow = words[::-1]

output = ''

for word in sdrow[:-1]: #takes whole list minus last space
    output += word #adds word from list
    output += " " #adds space
output += sdrow[-1] #tacks on the last word
print output
