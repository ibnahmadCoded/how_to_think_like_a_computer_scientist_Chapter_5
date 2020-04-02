def count_letters(letter, word, start=0):
    """
    Counts the number of a particular letter in a given word
    by using the find() function.
    """
    count = 0
    location = start
    tot = len(word)
    
    while location < tot:
        a = word.find(letter, location)   #word is found. find() returns -1 if unfound
        if a != -1:
            count += 1
            location = a + 1
    
    return count
