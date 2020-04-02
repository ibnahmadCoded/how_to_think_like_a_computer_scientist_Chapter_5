def double_stuff(stuff_list):
    """Overwrite each element of a list with double its value"""
    for (index, value) in enumerate(stuff_list):
        stuff_list[index] = value * 2
