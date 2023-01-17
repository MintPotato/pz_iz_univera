import matplotlib.pyplot as plt
import numpy as np
from numpy import cos, log2, log, sin


# функция возвращающая набор значений для исходной функции
def func(x):
    y = []
    for el in x:
        y += [(6 * log2(el / 10) * cos(6 * el / 10 - 10))]

    return y


# функция возвращающая набор значений для производной исходной функции
def pervaya_proizvod(x):
    y = []
    for el in x:
        el = el / 10
        y += [(6 * (cos(6 * el - 10) - 6 * el * log(el) * sin(6 * el - 10))) / (el * log(2))]

    return y


# функция возвращающая набор значений для второй производной исходной функции
def vtoraya_proizvod(x):
    y = []
    for el in x:
        el = el / 10
        y += [(-6 * (36 * (el ** 2) * log(el) + 1) * cos(6 * el - 10) - 72 * el * sin(6 * el - 10)) / (
                (el ** 2) * log(2))]

    return y


# функция возвращающая набор значений для нормали к точке функции
def normal(x):
    normaly = []
    k = x[27] / 10
    func_formula = 6 * log2(k) * cos(6 * k - 10)
    prozv_formula = (6 * (cos(6 * k - 10) - 6 * k * log(k) * sin(6 * k - 10))) / (k * log(2))

    for el in x:
        el = el / 10
        normaly += [func_formula - (el - k) / prozv_formula]

    return normaly


"""В случае когда назодится одна касательная, возвращает набор значений этой касательной к некоторой точки
Для случая когда надо найти множество касательных, сразу записывает их в график"""


def kasat(x, graph4=False):
    kasaty = []
    if not graph4:
        k = x[27] / 10
        func_formula = 6 * log2(k) * cos(6 * k - 10)
        prozv_formula = (6 * (cos(6 * k - 10) - 6 * k * log(k) * sin(6 * k - 10))) / (k * log(2))
        for el in x:
            el = el / 10
            kasaty += [func_formula + prozv_formula * (el - k)]
    else:
        for i in range(len(x)):
            k = x[i] / 10
            func_formula = 6 * log2(k) * cos(6 * k - 10)
            prozv_formula = (6 * (cos(6 * k - 10) - 6 * k * log(k) * sin(6 * k - 10))) / (k * log(2))
            for el in x:
                el = el / 10
                kasaty += [func_formula + prozv_formula * (el - k)]
            plt.plot(x, kasaty, color='r')
            kasaty = []

    return kasaty


# находит точки макс/мин для исходной функции
def spots_for_first_graph(y):
    maxy, miny = max(y), min(y)

    for point in range(len(y)):
        if y[point] == maxy:
            maxx = point + 1
        if y[point] == miny:
            minx = point + 1

    return (maxy, maxx), (miny, minx)


def perviy_graph(x):
    y = func(x)

    plt.plot(x, y)
    maxim, minim = spots_for_first_graph(y)
    plt.plot(maxim[1], maxim[0], 'o', color='b')
    plt.plot(minim[1], minim[0], 'o', color='b')
    y = normal(x)
    plt.plot(x, y, '--', color='g')
    y = kasat(x)
    plt.plot(x, y, '--', color='r')
    plt.plot(x[27], y[27], 'o', color='b')

    plt.show()


def graphic_perv_proizvod(x):
    y = pervaya_proizvod(x)
    plt.plot(x, y)
    plt.show()


def graphic_vtoroy_proizvod(x):
    y = vtoraya_proizvod(x)
    plt.plot(x, y)
    plt.show()


def graphic_kasat_rassl(x):
    y = func(x)
    plt.plot(x, y)
    y = kasat(x, True)
    plt.show()


#
def dlina_krivoy(x):
    y = func(x)
    dlina = 0
    for i in range(len(x) - 1):
        dlina += np.sqrt((x[i + 1] - x[i]) ** 2 + (y[i + 1] - y[i]) ** 2)

    print(dlina)


def main():
    x = [i for i in range(1, 51)]
    perviy_graph(x)
    graphic_perv_proizvod(x)
    graphic_vtoroy_proizvod(x)
    graphic_kasat_rassl(x)
    dlina_krivoy(x)


if __name__ == '__main__':
    main()
