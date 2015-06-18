# this script should take in a sentence or statement from the user,
# then repeat that statement back with the words in reverse order.
# Do not reverse the words themselves!

statement = raw_input("Please enter a statment to reverse.\n>> ")
min = 0
max = 0
words = []
reversed_statement = ""

for i in range(len(statement)):
    if statement[i] == " ":
        max = i
        words.append(statement[min:max])
        min = max + 1

words.append(statement[min:])

reversed_array = words[::-1]

for word in reversed_array[:-1]:
    reversed_statement += word
    reversed_statement += ' '

reversed_statement += reversed_array[-1]

print reversed_statement










