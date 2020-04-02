def table_of_letters(data):
    s = data.lower()

    new_text = {}
    for letter in s:
        new_text[letter] = new_text.get(letter, 0) + 1

    items = list(new_text.items())

    items.sort()
    for (item, count) in items:
        if item != " ":
            print(item, "\t", count)
        
