#  TODO: ADVANCED
#  This reads lines from the input file reverses their order and writes them into the output file.
# How could we do this without the "all" variable,
#  so we do not wast ram memory by loading the whole file.

import fileinput

for line in fileinput.input("input_data.txt"):

    line = open("input_data.txt").read().splitlines()

    line = line[::-1]

    print line






    # input_file = open("input_data.txt", "r")
    # output_file = open("input_data.txt", "w")
    #
    # End_of_file = 2
    #
    # input_file.seek(0, End_of_file)
    # length = input_file.tell()
    #
    # index = length
    # line = ""
    #
    # while index >= 0:
    #     i = index
    #     input_file.seek(i)
    #     c = input_file.read(1)
    #
    #     if c == "\n":
    #         print(line)
    #         output_file.write(line + "\n")
    #         line = ""
    #     else:
    #         line = c + line
    #     index -= 1
    #
    # print(line)
    # output_file.write(line + "\n")
    # input_file.close()
    # output_file.close()








#
# input_file = open("input_data.txt", "r")
#
# line = input_file.readline()
# all = []
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
#
# print all
#