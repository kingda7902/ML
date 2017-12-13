# coding: utf-8
import numpy as np
from random import randint

def make_matrix_file( n, m, output_file="./matricA.txt", interval=[0,9] ):
    matrix = np.random.randint( interval[0], interval[1] + 1, size=[n,m])
    np.savetxt(output_file, matrix, fmt="%d")
    return True
def output_ans(file_A,file_B):
    matrix_A = np.loadtxt( file_A, dtype=int)
    matrix_B = np.loadtxt( file_B, dtype=int)
    ans_one = matrix_A.dot(matrix_B).reshape([1,-1])
    ans_one.sort()
    count = 1
    with open('./ans_one.txt', 'wt') as f:
        for elt in np.nditer(ans_one):
            f.write('{} {}\n'.format(count, elt))
            count += 1
    return True
