def string_to_ascii(s):
    output = []
    for c in s:
        v = ord(c)
        # opposite of chr
        output.append(v)
        print(bin(v))
    return output

print(string_to_ascii("Jake"))
print(string_to_ascii("Obadiah"))
print(string_to_ascii("Richmond"))
print(string_to_ascii("JOR"))
