def scalar_mult(scalar, vector):
    """multiplies scalar by vector"""
    new_vector = []
    for i, v in enumerate(vector):
        new_vector.append(scalar * vector[i])

    return new_vector
