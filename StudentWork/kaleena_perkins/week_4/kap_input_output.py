#  TODO: ADVANCED
#  This reads lines from the input file reverses their order and writes them into the output file.
# How could we do this without the "all" variable,
#  so we do not wast ram memory by loading the whole file.
import fileinput
#input_file = open("kap_input_data.txt", "r")

#~ line = input_file.readline()
#~ all = []
#~ while line:
    #~ all.append(line)
    #~ line = input_file.readline()
#~ all.append(line)
#~ input_file.close()
#~ 
#~ # reverse the order
#~ all.reverse()
#~ 
output_file = open("output_data.txt", "a")
#~ 
#~ for line in all:
    #~ output_file.write(line + "\n")
#~ output_file.close()


for line in fileinput.input("kap_input_data.txt"):
	#find a way to prepend to file without overwriting it
	output_file.seek(0)
	output_file.write('\n' + line)
		
	
output_file.close()
