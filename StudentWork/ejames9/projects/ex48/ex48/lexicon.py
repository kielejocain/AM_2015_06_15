

lexicon = {
    'direction': ['north', 'south', 'east', 'west',
        'down', 'up', 'left', 'right', 'back'],
    'verb': ['go', 'stop', 'kill', 'eat'],
    'stop': ['the', 'in', 'of', 'from', 'at', 'it'],
    'noun': ['door', 'bear', 'princess', 'cabinet']
}


def scan(sentence):

    results = []

    list = sentence.split(' ')

    for word in list:
        if word.isdigit():
            results.append(('number', int(word)))
            continue

        for category in lexicon:
            if word in lexicon[category]:
                results.append((category, word))
                break
        else:
            results.append(('error', word))

    return results
