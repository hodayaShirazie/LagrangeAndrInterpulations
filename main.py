from colors import bcolors
from liniar import linearInterpolation
from polinomial import polynomialInterpolation
from lagrange import lagrange_interpolation


if __name__ == '__main__':
    a = (1, 3)
    b = (2, 4)
    c = (3, -1)

    x = 1.2
    table_points = [a, b, c]

    print(bcolors.OKBLUE,"1- liniar interpolation \n 2- polinomial interpolation \n 3- lagrange interpolation")
    nav = int(input())

    if(nav == 1):
        linearInterpolation(table_points, x)

    elif(nav == 2):
        polynomialInterpolation(table_points, x)

    elif (nav == 3):
        lagrange_interpolation(table_points, x)



