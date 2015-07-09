#  TODO: ADVANCED
#  This reads lines from the input file reverses their order and writes them into the output file.
# How could we do this without the "all" variable,
#  so we do not wast ram memory by loading hte whole file.




input_file = open("input_data.txt", "r")
output_file = open("output_data.txt", "w")

#for c in line
# if c == "\n" line seek point to that point. count bytes until
input_file.seek(0,2)
file_length = input_file.tell()
location = -1
line = ""
#size = input_file.read()
for byte in range(file_length):
    input_file.seek(location, 2)
    c = input_file.read(1)
    if c != "\n":
        line = c + line
    else:
        output_file.write(line + "\n")
        line = ""
    location -= 1
output_file.write(line + "\n")

input_file.close()
output_file.close()
