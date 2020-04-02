def dot_product(vector1, vector2):
    """returns the sum of the product of corresponding
    elements of two vectors of same length"""
    new_vector = []
    dot_product = 0
    
    if len(vector1) == len(vector2):
        for index, value in enumerate(vector1):
            new_vector.append(vector1[index] * vector2[index])

        for i in range(len(new_vector)):
            dot_product += new_vector[i]

    return dot_product
