
import numpy as np
from Res.task12_func import gen_rand_matrix
import random

rows = random.randint(1, 8)
cols = rows

matrix = gen_rand_matrix(rows, cols, -50, 50)
np_matrix = np.array(matrix).transpose()

determinant = np.linalg.det(np_matrix)
print(np_matrix)
print(determinant)  # Interesting numerical errors
