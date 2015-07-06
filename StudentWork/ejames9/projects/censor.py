def censor(text, word):
    words2 = []
    words = text.split(" ")
    print words
    print word
    for w in words:
        if w == word:
            words2.append('*' * len(w))
        else:
            words2.append(w)



    result = " ".join(words2)
    print result

censor("fuck go fuck yourself fuck .", "fuck")
