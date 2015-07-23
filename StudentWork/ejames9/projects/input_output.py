#  TODO: ADVANCED
#  This reads lines from the input file reverses their order and writes them into the output file.
# How could we do this without the "all" variable,
#  so we do not wast ram memory by loading hte whole file.

input_file = open("input_data.txt", "r")
lines = input_file

output_file = open("output_data.txt", "w")

lines.seek(0, 2)
length = lines.tell()
index = length

line = ""

while index >= 0:
    i = index
    lines.seek(i)
    c = lines.read(1)

    if c == "\n":
        print line
        output_file.write(line + "\n")
        line = ""
    else:
        line = c + line
    index -= 1

print line
output_file.write(line + "\n")

input_file.close()
output_file.close()
















