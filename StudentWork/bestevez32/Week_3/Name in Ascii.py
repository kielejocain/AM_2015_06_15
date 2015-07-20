s = "BJE"

for c in s:
        print c
        print ord(c)

for string_to_ascii in (s):
    output = []
    for c in s:
        v = ord(c)
        # opposite of chr
        output.append(v)
        print(bin(v))
        return output

print(string_to_ascii("BJE"))
print(string_to_ascii("Brandon"))
