from colors import bcolors


def linearInterpolation(table_points, point):
    flag = 1
    if (point < table_points[0][0]):
        i = 0
        flag = 0
    else:
        if (point > table_points[len(table_points) - 1][0]):
            i = len(table_points) - 2
            flag = 0
    if(not flag):
        x1 = table_points[i][0]
        x2 = table_points[1 + 1][0]
        y1 = table_points[i][1]
        y2 = table_points[i + 1][1]

        result = ((point - x2) / (x1 - x2)) * y1 + ((point - x1) / (x2 - x1)) * y2

        print(bcolors.OKGREEN, "\nThe approximation (extrapolation) of the point ", point, " is: ", bcolors.ENDC,
              round(result, 4))
    else:
        p = []
        for i in range(len(table_points) - 1):
            if table_points[i][0] <= point <= table_points[i+1][0]:
                x1 = table_points[i][0]
                x2 = table_points[i + 1][0]
                y1 = table_points[i][1]
                y2 = table_points[i + 1][1]

                result = ((point - x2)/(x1-x2))*y1 + ((point - x1)/(x2-x1))*y2
                print(bcolors.OKBLUE,"---------------------------------------------------------------------------------------------------------")
                print(bcolors.OKBLUE, "liniar interpolation", bcolors.ENDC)
                print(bcolors.OKGREEN, "\nThe approximation (interpolation) of the point ", point, " is: ",bcolors.ENDC, round(result, 4))
                print(bcolors.OKBLUE,"---------------------------------------------------------------------------------------------------------")


if __name__ == '__main__':
    a = (1, 3)
    b = (2, 4)
    c = (3, -1)

    x = 1.2

    table_points = [a, b, c]
    linearInterpolation(table_points, x)
