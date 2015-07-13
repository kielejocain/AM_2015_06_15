#  TODO: ADVANCED
#  This reads lines from the input file reverses their order and writes them into the output file.
#  How could we do this without the "all" variable,
#  so we do not waste ram memory by loading the whole file.

input_file = open("input_data.txt", "r")

line = input_file.readline()
all = []
while line:
    all.append(line)
    line = input_file.readline()
all.append(line)
input_file.close()

# reverse the order
all.reverse()

output_file = open("output_data.txt", "w")

for line in all:
    output_file.write(line + "\n")
output_file.close()

#####

# IDEAS:

# 1. find all \n breakpoints, gather line from end of file via
# generator & append to new file
# 2. read each line as normal & insert at beginning of new file
# 3. use enumerate to find # of lines, then read them backwards
# 4. Reverse the whole file, flip each line back as it's written

#####

# input_file = open("input_data.txt", "r")
# last_line = 0
#
# # Find total number of lines
# for i, line in enumerate(input_file):
#     last_line = i
#     print i
# total_lines = last_line
#
# # Generate lines back-to-front
# def generate_line(input_file, last_line):
#     for i, line in enumerate(input_file):
#         if i == last_line:
#             last_line -= 1
#             print line
#             yield line
#
# # write lines
# output_file = open("output_data.txt", "w")
# for i in range(total_lines + 1):
#     line = generate_line(input_file, last_line)
#     output_file.write(str(line))
#
# # Close files
# input_file.close()
# output_file.close()

###### Readline reversed

import os

# Open both files
input_file = open("input_data.txt", "r")
output_file = open("output_data.txt", "w")

# Find file size
file_info = os.stat("input_data.txt")
file_size = file_info.st_size

# ### Better alternative:
# input_file.seek(0, END_OF_FILE)
# file_size = input_file.tell()

# go to end of file
END_OF_FILE = 2
location = -1
current_line = ""

for char in range(file_size):
    input_file.seek(location, END_OF_FILE)
    current_char = input_file.read(1)
    if current_char != "\n":
        current_line = current_char + current_line
    else:
        output_file.write(current_line + "\n")
        current_line = ""
    location -= 1

# add last line, as it doesn't have a \n
output_file.write(current_line)

# close files
input_file.close()
output_file.close()