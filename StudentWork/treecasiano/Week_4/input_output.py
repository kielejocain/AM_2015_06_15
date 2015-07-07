#  TODO: ADVANCED
# This reads lines from the input file reverses their order and writes them into the output file.
# How could we do this without the "all" variable,
# so we do not waste ram memory by loading the whole file.

# input_file = open("input_data.txt", "r")
#
# line = input_file.readline()
# all = []
#
# while line:
#     all.append(line)
#     line = input_file.readline()
# all.append(line)
# input_file.close()
#
# # reverse the order
# all.reverse()
#
# output_file = open("output_data.txt", "w")
#
# for line in all:
#     output_file.write(line + "\n")
# output_file.close()



input_file = open("input_data.txt", "r")
output_file = open("output_data.txt", "w")

# 2 indicates to seek till the end of the file
END_OF_FILE = 2
input_file.seek(0, END_OF_FILE)
# tell() lets us know our location in the file
# which is the same as the number of characters
length = input_file.tell()

# seek to 0 from the end
index = length
line = ""

while index >= 0:
    i = index
    input_file.seek(i)
    c = input_file.read(1)

    if c == "\n":
        output_file.write(line + "\n")
        line = ""  # we reset the line here
    # if the character is not \n, we will keep adding
    # to the front of the string
    else:
        line = c + line
    # decrementing the index allows us to iterate backwards
    index -= 1

# since the last line does not have \n, we have to add after the loop
output_file.write(line + "\n")

input_file.close()
output_file.close()
