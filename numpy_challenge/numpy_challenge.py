# Installing and importing numpy

!pip install numpy

import numpy as np

# Creating the arrays

data = [1, 2, 3]
my_first_array = np.array(data) # The first way is making the array from existing data

my_second_array = np.full(8, 8) # Creating the array from zero. We get array with 8 eights

my_third_array = np.arrange(1, 10, 2) # We get the array from 1 to 10 with the step 2

# Creating matrix_multiplication

def matrix_multiplication(m1, m2):
    return np.dot(m1, m2)

# Creating multiplication_check

def multiplication_check(ms):
    result = True
    for i in range(len(ms)):
        if i > 0:
            shape_prev = ms[i-1].shape
            shape_i = ms[i].shape
            if shape_prev[1] != shape_i[0]:
                result = False
    return result

# Creating multiply_matrices

def multiply_matrices(ms):
    if multiplication_check(ms):
        result = ms[0]
        for i in range(len(ms)):
            if i > 0:
                result = matrix_multiplication(result, ms[i])
        return result
    else:
        return None

# Creating compute_2d_distance

def compute_2d_distance(v1, v2):
    a1 = np.array(v1)
    a2 = np.array(v2)
    vector = a1 - a2
    return ((vector[0])**2 + vector[1])**2)**0.5

# Creating compute_multidimensional_distance

def compute_multidimensional_distance(v1, v2):
    a1 = np.array(v1)
    a2 = np.array(v2)
    vector = a1 - a2
    sq = 0
    for i in vector:
        sq + = i**2
    return sq**0.5

# Creating compute_pair_distances

def compute_pair_distances(m):

