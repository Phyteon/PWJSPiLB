
import numpy as np
from Res.task12_func import gen_rand_matrix

cols = 8
rows = 8

matA = gen_rand_matrix(rows, cols, -50, 50)
matB = gen_rand_matrix(rows, cols, -50, 50)
np_matA = np.array(matA).transpose()
np_matB = np.array(matB).transpose()
outcome = np_matA.dot(np_matB)
print(outcome)
