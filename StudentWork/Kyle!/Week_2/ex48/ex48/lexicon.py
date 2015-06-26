# define our word categories
lexicon = {
    'direction': ['north', 'south', 'east', 'west',
        'down', 'up', 'left', 'right', 'back'],
    'verb': ['go', 'stop', 'kill', 'eat'],
    'stop': ['the', 'in', 'of', 'from', 'at', 'it'],
    'noun': ['door', 'bear', 'princess', 'cabinet']
}

# build a function to deal with numbers
def convert_number(s):
    """Unnecessary test of whether a string is a representation of an integer"""
    try: # if the string can be converted to an int, return the result
        return int(s)
    except ValueError: # otherwise, return None
        return None

def scan(sentence):
    # split your sentence into words at spaces
    words = sentence.split()
    # prepare the container for our results
    results = []
    # for each word in our sentence:
    for word in words:
        if word.isdigit(): # or if convert_number(word) is not None:
            # if it's a number, say so and move on
            results.append(('number', int(word)))
            continue
        # if it's not a number, see if it fits in a category
        for category in lexicon:
            if word in lexicon[category]:
                results.append((category, word))
                break
        else: # i.e., no break
            # if if fits in no category, call it an 'error'
            results.append(('error', word))
    return results
