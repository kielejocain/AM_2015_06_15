name = 'AHK' # 65 72 75
ascii = [65, 72, 75]

def string_to_ascii(word):
    for char in word:
        print ord(char)

def ascii_to_string(list):
    for num in list:
        print chr(num)

def num_to_binary(word):
    for char in word:
        print bin(char)

string_to_ascii(name)
ascii_to_string(ascii)
num_to_binary(ascii)