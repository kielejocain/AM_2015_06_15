#  TODO: ADVANCED
#  This reads lines from the input file, reverses their order and writes them into the output file.
# How could we do this without the "all" variable,
#  so we do not waste ram memory by loading the whole file.
"""
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

#simple solution, but still reads in the entire file
#input_file = open("input_data.txt", "r")
#for line in reversed(input_file.readlines()):
#        print line
#input_file.close()
"""

class ReverseReader(object):
    """Reads a text file from the last bit backward, parsing lines as it encounters
    newline characters."""
    FIRST_CHARACTER = 1
    def __init__(self, filename):
        self.file = open(filename, "r")
        self.char_buffer = []

        self.file.seek(0, 2) #go to the end of the file
        self.filesize = self.file.tell()

    def readline(self):
        index = 1
        while True:
            self.file.seek(-index, 2)
            char = self.file.read(1)
            self.char_buffer.append(char)
            if char == '\n' or self.file.tell() == ReverseReader.FIRST_CHARACTER:
                line = "".join(reversed(self.char_buffer))
                self.char_buffer = []
                print line
            index += 1
            break


    def readlines(self):
            index = 1
            while index <= self.filesize:
                self.file.seek(-index, 2) #next byte from the end
                char = self.file.read(1)
                self.char_buffer.append(char)
                if char == '\n' or self.file.tell() == ReverseReader.FIRST_CHARACTER:
                    line = "".join(reversed(self.char_buffer))
                    self.char_buffer = []
                    print line
                index += 1

def test_ReverseReader():
    rr = ReverseReader("/media/evan/400ABF960ABF8804/code_guild/StudentWork/palmerev/input_data.txt")
    rr.readlines()


test_ReverseReader()
