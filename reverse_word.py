def reverse(word):
    """Reverses word given as argument"""
    new_word = ""
    step = len(word) + 1
    count = 1

    while step - count != 0:
        new_word += word[count * -1]
        count += 1

    return new_word
        
