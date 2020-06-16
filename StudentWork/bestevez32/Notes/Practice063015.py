characters = "ABCDEF"
character_goal = "FEDCBA"

# Define a function character_outcome with the variable characters.
def reversed_characters(characters):
    output = ""
    for c in characters:
        output = c + output
    return output

print(reversed_characters(characters))

