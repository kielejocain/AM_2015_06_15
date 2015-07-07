#  TODO: ADVANCED
#  This reads lines from the input file reverses their order and writes them into the output file.
# How could we do this without the "all" variable,
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
