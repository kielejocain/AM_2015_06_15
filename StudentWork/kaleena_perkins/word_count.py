my_dict = {}

string = raw_input("String?")

def word_count(string):
  string.lower()
  string_list = string.split()
  for word in string_list:
    if word in my_dict:
      my_dict[word] += 1
    else:
      word_count = 1
      my_dict.update({word: word_count})
  return my_dict
      

word_count(string)
print my_dict
