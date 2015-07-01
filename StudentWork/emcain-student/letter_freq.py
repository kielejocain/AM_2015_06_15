__author__ = 'Emily'

from string import lowercase

sentence = "Now is the time for all good people to come to the aid of their planet."

def letter_analysis(phrase):
    letter_dict = {}
    for letter in phrase.lower():
        if letter not in letter_dict.keys():
            letter_dict[letter] = 0
        letter_dict[letter] += 1
    return letter_dict

def letter_display(ltr_dct):
    output = ""
    for c in lowercase[:]:
        if c in ltr_dct.keys() and ltr_dct[c] > 1:
            output += c + " occurs " + str(ltr_dct[c]) + " times.\n"
        elif c in ltr_dct.keys() and ltr_dct[c] == 1:
            output += c + " occurs once.\n"
        else:
            output += c + " is not in the string.\n"
    return output

print letter_display(letter_analysis(sentence))
