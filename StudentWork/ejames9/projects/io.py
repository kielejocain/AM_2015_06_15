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
    else:
        line = c + line
    i -= 1

print line
output_file.write(line + "\n")

input_file.close()
output_file.close()
