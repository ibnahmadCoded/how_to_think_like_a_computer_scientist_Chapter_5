def count_letters(word, letter):
    """
    Counts the number of a particular letter in a given word"""
    count = 0
    for leta in word:
        if leta == letter:
            count += 1
    return count
