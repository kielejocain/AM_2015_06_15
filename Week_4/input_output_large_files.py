#  TODO: ADVANCED
#  This reads lines from the input file reverses their order and writes them into the output file.
# How could we do this without the "all" variable,
#  so we do not waste ram memory by loading the whole file.

input_file = open("input_data.txt", "r")
output_file = open("output_data.txt", "w")

CURRENT_POSITION = 1
END_OF_FILE = 2
input_file.seek(0, END_OF_FILE)
length = input_file.tell()
# seek to 0 from the end
index = length
line = ""
while index >= 0:
    i = index
    input_file.seek(i)
    c = input_file.read(1)
    if c == "\n":
        print(line)
        output_file.write(line + "\n")
        line = ""
    else:
        line = c + line
    index -= 1
print(line)
output_file.write(line + "\n")
input_file.close()
output_file.close()
