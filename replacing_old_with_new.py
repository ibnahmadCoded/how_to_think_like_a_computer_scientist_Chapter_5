def replace(s, old, new):
    """replaces all occurences of old with new in a string s"""
    components = s.split(old)

    return new.join(components)
