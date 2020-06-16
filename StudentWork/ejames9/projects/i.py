
lexicon = {
    'direction': ['north', 'south', 'east', 'west',
        'down', 'up', 'left', 'right', 'back'],
    'verb': ['go', 'stop', 'kill', 'eat'],
    'stop': ['the', 'in', 'of', 'from', 'at', 'it'],
    'noun': ['door', 'bear', 'princess', 'cabinet']
}


def scan(sentence):

    results = []

    sentence = raw_input(">> ")

    list = sentence.split(' ')

    for word in list:
        if word.isdigit():
            results.append(('number', int(word)))
            continue

            for category in lexicon:
                if word in lexicon:
                    results.append((category, word))
                    break
                else:
                    results.append(('error', word))

    return results


scan('I will go north and south to kill and eat a from a princess bear.')
