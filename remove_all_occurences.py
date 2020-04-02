def remove_letter(letter, word):
    """removes all occurences of a letter from a word given as argument"""
    new_word = ""

    for leta in word:
        if leta != letter:
            new_word += leta

    return new_word
        
