from colors import bcolors
from gaussian_elimination import gaussianElimination



def polynomialInterpolation(table_points, x):

    n = len(table_points)
    matrix = [[0] * (n + 1) for _ in range(n)]
    for i in range(n):
        x_i = table_points[i][0]
        y_i = table_points[i][1]
        for j in range(n):
            matrix[i][j] = x_i ** j
        matrix[i][-1] = y_i

    result = gaussianElimination(matrix)
    if isinstance(result, str):
        print(result)

    result2 = sum (result[i] * (x ** i) for i in range(n))

    print(bcolors.OKBLUE,"---------------------------------------------------------------------------------------------------------")
    print(bcolors.OKBLUE, "polinomial interpolation", bcolors.ENDC)
    print(bcolors.OKGREEN, f"\nThe Result of P(X={x}) is:", bcolors.ENDC)
    print(result2)
    print(bcolors.OKBLUE,"---------------------------------------------------------------------------------------------------------")






if __name__ == '__main__':
    a = (1, 3)
    b = (2, 4)
    c = (3, -1)

    x = 1.2

    table_points = [a, b, c]
    polynomialInterpolation(table_points, x)