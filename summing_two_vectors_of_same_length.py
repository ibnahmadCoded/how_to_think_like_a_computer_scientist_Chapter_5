def add_vectors(vector1, vector2):
    """Sums corresponding elements of two vectors of same lenght"""
    vectors_sum = []
    
    if len(vector1) == len(vector2):
        #the two vectors are of same lenght
        for i in range(len(vector1)):
            vectors_sum.append(vector1[i] + vector2[i])

    return vectors_sum 
            
    
