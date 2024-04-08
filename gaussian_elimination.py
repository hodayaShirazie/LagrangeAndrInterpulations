import numpy as np
from colors import bcolors


def swap_row(mat, i, j):
    N = len(mat)
    for k in range(N + 1):
        temp = mat[i][k]
        mat[i][k] = mat[j][k]
        mat[j][k] = temp


def gaussianElimination(mat):
    N = len(mat)

    singular_flag = forward_substitution(mat)

    if singular_flag != -1:

        if mat[singular_flag][N]:
            return "Singular Matrix (Inconsistent System)"
        else:
            return "Singular Matrix (May have infinitely many solutions)"

    return backward_substitution(mat)




def forward_substitution(mat):
    N = len(mat)
    for k in range(N):

        pivot_row = k
        v_max = mat[pivot_row][k]
        for i in range(k + 1, N):
            if abs(mat[i][k]) > v_max:
                v_max = mat[i][k]
                pivot_row = i


        if not mat[k][pivot_row]:
            return k

        if pivot_row != k:
            swap_row(mat, k, pivot_row)

        for i in range(k + 1, N):

            m = mat[i][k] / mat[k][k]

            for j in range(k + 1, N + 1):
                mat[i][j] -= mat[k][j] * m

            mat[i][k] = 0

    return -1


def backward_substitution(mat):
    N = len(mat)
    x = np.zeros(N)

    for i in range(N - 1, -1, -1):

        x[i] = mat[i][N]

        for j in range(i + 1, N):
            x[i] -= mat[i][j] * x[j]

        x[i] = (x[i] / mat[i][i])

    return x

