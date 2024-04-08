from colors import bcolors


def lagrange_interpolation(table_points, x):

    n = len(table_points)
    result = 0.0

    for i in range(n):
        term = table_points[i][1]
        for j in range(n):
            if i != j:
                term *= (x - table_points[j][0]) / (table_points[i][0] - table_points[j][0])
        result += term

    print(bcolors.OKBLUE,"---------------------------------------------------------------------------------------------------------")
    print(bcolors.OKBLUE, "lagrange interpolation", bcolors.ENDC)
    print(bcolors.OKGREEN, f"\nThe Result of P(X={x}) is:", bcolors.ENDC)
    print(result)


    print(bcolors.OKBLUE,"---------------------------------------------------------------------------------------------------------")

if __name__ == '__main__':
    a = (1, 3)
    b = (2, 4)
    c = (3, -1)

    x = 1.2

    table_points = [a, b, c]
    lagrange_interpolation(table_points, x)
