
import random as rn


def gen_rand_matrix(rows, cols, min, max):
    columns = []
    for i in range(0, cols):
        column = []
        for k in range(0, rows):
            column.append(rn.randint(min, max))
        columns.append(column)
    return columns
