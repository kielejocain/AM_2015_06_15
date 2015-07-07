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

input_file = open("input_data.txt", "r")
last_line = 0

# Find total number of lines
for i, line in enumerate(input_file):
    last_line = i
    print i
total_lines = last_line

# Generate lines back-to-front
def generate_line(input_file, last_line):
    for i, line in enumerate(input_file):
        if i == last_line:
            last_line -= 1
            print line
            yield line

# write lines
output_file = open("output_data.txt", "w")
for i in range(total_lines + 1):
    line = generate_line(input_file, last_line)
    output_file.write(str(line))

# Close files
input_file.close()
output_file.close()

###### Readline reversed

import os

input_file = open("input_data.txt", "r")
# go to end of file
location = -1
current_line = ""
not_done = True

while not_done:
    current_byte = input_file.seek(location, 2)
    print current_byte
    if current_byte != "\n":
        current_line += str(current_byte)
    location -= 1

