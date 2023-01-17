import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos, log2, log
import random


# f(x) = sin(x)*(cos((x^2)+5)); 0<=x<=5
def Function(x):
    y = []
    for i in range(len(x)):
        k = x[i]
        y.append(np.round(10 * log2(8 * k) * cos(((k ** 2) / 10) + 4) * 2 ** k))
    return y


def Length(x, y):
    length = 0
    for n in range(1, len(x)):
        length += np.sqrt((x[n] - x[n - 1]) ** 2 + (y[n] - y[n - 1]) ** 2)
    return length


"""def LengthVer2(pointA, pointB):
    finish_var = First_Derivative([pointB])[0]
    start_var = First_Derivative([pointA])[0]
    print(start_var, finish_var)
    finish = np.log(abs(np.sqrt(1+(finish_var**2))+finish_var))/2 + finish_var*np.sqrt(finish_var**2 + 1)/2
    start = np.log(abs(np.sqrt(1+(start_var**2))+start_var))/2 + start_var*np.sqrt(start_var**2 + 1)/2
    print(finish, start, finish-start)
    return finish-start"""


def First_Derivative(x):
    deff_y = []
    for i in x:
        deff_y.append(-((i ** 2) * (2 ** (i + 1)) * log(8 * i) * sin(((i ** 2) / 10) + 4) + (
                    -5 * log(2) * i * (2 ** (i + 1)) * log(8 * i) - 5 * (2 ** (i + 1))) * cos(((i ** 2) / 10) + 4)) / (
                                  log(2) * i))
    return deff_y


def Second_Derivative(x):
    deff_y = []

    for i in x:
        k = (i ** 2) / 10 + 4
        deff_y.append(-(((20 * log(2) * (i ** 3) + 10 * (i ** 2)) * (2 ** i) * log(8 * i) + 5 * (i ** 2) * (
                    2 ** (i + 2))) * sin(k) + ((2 * (i ** 4)) - 50 * (log(2) * log(2)) * (i ** 2)) * (2 ** i) * log(
            8 * i) + (50 - 100 * log(2) * i) * (2 ** i)) * cos(k) / (5 * log(2) * (i ** 2)))
    return deff_y


def Tangent(y, diff_y, x, x0, area, coloring="g"):
    k = x.index(x0)
    rangeForFuncX = 1
    rangeForFuncY = 3
    difference_right, difference_left = 0, 0
    function = [y + -diff_y * (x[k] - x0)]
    while (0 < k - difference_left or difference_right + k + 1 < len(x)):
        if k - (difference_left + 1) >= 0:
            difference_left += 1
            function[:0] = [y + diff_y * (x[k - difference_left] - x0)]
        if k + (difference_right + 1) < len(x):
            difference_right += 1
            function.append(y + diff_y * (x[k + difference_right] - x0))

    area.plot(x[k - (difference_left):k + difference_right + 1], function, color=coloring)
    return area


def math():
    x = [x / 10 for x in range(1, 51)]
    y = Function(x)
    y_diff_1 = First_Derivative(x)
    y_diff_2 = Second_Derivative(x)
    drawing(x, y, y_diff_1, y_diff_2)


def drawing(x, y, y_diff_1, y_diff_2):
    figure, axis = plt.subplots(2, 2)
    axis[0, 0].axhline(y=0, color='k')
    axis[0, 0].axvline(x=0, color='k')
    axis[0, 1].axhline(y=0, color='k')
    axis[0, 1].axvline(x=0, color='k')
    axis[1, 0].axhline(y=0, color='k')
    axis[1, 0].axvline(x=0, color='k')
    axis[1, 1].axhline(y=0, color='k')
    axis[1, 1].axvline(x=0, color='k')

    # For Function
    axis[0, 0].plot(x, y)
    axis[0, 0].set_title("Function")
    maxY = max(y)
    minY = min(y)
    for n in range(len(x)):
        if y[n] == maxY:
            maxX = x[n]
        if y[n] == minY:
            minX = x[n]

    axis[0, 0].plot(maxX, maxY, 'o', color='b')
    axis[0, 0].plot(minX, minY, 'o', color='b')
    x0 = random.randint(min(x) * 10, max(x) * 10)
    axis[0, 0] = Tangent(y[x0], y_diff_1[x0], x, x[x0], axis[0, 0], "r")
    axis[0, 0] = Tangent(y[x0], (-1 / y_diff_1[x0]), x, x[x0], axis[0, 0], "c")
    axis[0, 0].plot(x[x0], y[x0], 'o', color='b')

    # For First derivative of Function
    axis[0, 1].plot(x, y_diff_1)
    axis[0, 1].set_title("First derivative of Function")

    # For Second derivative of Function
    axis[1, 0].plot(x, y_diff_2)
    axis[1, 0].set_title("Second derivative of Function")

    axis[1, 1].set_title("Tangential stratification")
    for n in range(1, len(x)):
        axis[1, 1] = Tangent(y[n], y_diff_1[n], x, x[n], axis[1, 1])
        axis[1, 1].plot(x[n], y[n], 'o', color='b')
    axis[1, 1].plot(x, y, color="r")
    length = Length(x, y)

    axis[0, 0].set_xlabel('Length: ' + str(round(length)))
    print(length)
    # print(LengthVer2(0,5))
    plt.show()


def main():
    math()


if __name__ == "__main__":
    main()