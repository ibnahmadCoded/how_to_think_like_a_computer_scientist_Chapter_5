def cross_product(vector1, vector2):
    """calculates cross product of two vectors of length 3"""
    if len(vector1) == len(vector2) == 3: #check if both vector lengths are 3
        #create new_vector containing all lsit values
        new_vector = vector1[:]
        new_vector.extend(vector2)

        #calculate determinants for cross_product
        det1 = (new_vector[1] * new_vector[5])-(new_vector[2] * new_vector[4])
        det2 = (new_vector[0] * new_vector[1])-(new_vector[2] * new_vector[3])
        det3 = (new_vector[0] * new_vector[4])-(new_vector[1] * new_vector[3])

        result = [det1, det2 * -1, det3]

        return result
