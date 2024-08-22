def single_root_words(root_word, *other_words):
    same_words = []
    for key in other_words:
        if root_word.lower() in key.lower() or key.lower() in root_word.lower():
            same_words.append(key)
    return same_words
#end of single_root_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words('Dis', 'Able', 'Distance', 'Disable', 'Bagel','distribution', 'discover')
result4 = single_root_words('Ата', 'Атака', 'Африка', 'Атас', 'Атилла','Атос')


print(result1)
print(result2)
print(result3)
print(result4)
