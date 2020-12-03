
from Res.task12_func import gen_rand_matrix
import copy

rows = 128
cols = 128

mat1 = gen_rand_matrix(rows, cols, -50, 50)
mat2 = gen_rand_matrix(rows, cols, -50, 50)

outcome = copy.deepcopy(mat1)

for i in range(0, cols):
    for k in range(0, rows):
        outcome[i][k] = mat1[i][k] + mat2[i][k]

