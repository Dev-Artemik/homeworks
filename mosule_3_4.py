def single_root_words(root_word, *other_words):
    same_words = []
    root_word_l = root_word.lower()
    for word in other_words:
        word_l = word.lower()
        if word_l in root_word_l:
            same_words.append(word)
        elif root_word_l in word_l:
            same_words.append(word)
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)