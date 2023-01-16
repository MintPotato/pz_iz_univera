import copy
import time


def main():
    global L, N
    f = open('input.txt')
    a = list(f)
    NLK, figure_place = list(map(int, a[0].split())), a[1:]
    f.close()
    start_time = time.time()
    L, N = NLK[1], NLK[0]

    ishod_doska = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(NLK[-1]):
        coords = list(map(int, figure_place[i].split()))
        ishod_doska[coords[0]][coords[1]] = '#'
        ishod_doska = boi_figuri(ishod_doska, coords[0], coords[1], flag=True)

    svobodn_mesta = 0

    for i in range(len(ishod_doska)):
        svobodn_mesta += ishod_doska[i].count(0)
        ishod_doska[i] = tuple(ishod_doska[i])

    if svobodn_mesta > L:
        f1 = open('output.txt', 'w')

        rasstanovka_figur(tuple(ishod_doska), 0, f1, 0, flag=False)
        f1.close()
        if kolvo_otvet:
            print(kolvo_otvet)
        else:
            print('ns')

    else:
        print('ns')
    print(time.time() - start_time)


# рекурентная функция расставляющая фигуры на доску
def rasstanovka_figur(doska: tuple[tuple], cnt: int, file, a=0, b=0, flag=True):
    global L, N, otvet, console_doska, kolvo_otvet

    if flag:
        doska = list(doska)
        c = list(doska[a])
        c[b] = '#'
        doska[a] = tuple(c)
        doska = boi_figuri(doska, a, b)
    # если количество расставленных фигур, не включая исходные, меньше заданного, то продолжаем расставлять
    if cnt < L:
        for i in range(a, N):
            for j in range(b, N):
                if doska[i][j] == 0:
                    # dop_doska = copy.copy(doska)
                    # c = list(dop_doska[i])
                    # c[j] = '#'
                    # dop_doska[i] = tuple(c)
                    # dop_doska = boi_figuri(dop_doska, i, j)

                    rasstanovka_figur(doska, cnt + 1, file, i, j)
            b = 0

    # если количество фигур выставленных на доске равно искомому, то записываем координаты фигур в ответ
    elif cnt == L:
        kolvo_otvet += 1
        figures = figuri_na_doske(doska)
        file.write('{}\n'.format(figures))
        if not console_doska:
            vyvod_doski_v_konsol(doska)
            console_doska = True


# функция возвращающая координаты фигур расставленных на доске
def figuri_na_doske(doska: list[list]) -> list[tuple]:
    coords = ''
    for i in range(N):
        for j in range(N):
            if doska[i][j] == '#':
                coords += '({}, {}) '.format(i, j)

    return coords.strip()


# zapoln kletok boya
def boi_figuri(doska: list[tuple], i: int, j: int, flag=False) -> list[list]:
    if not flag:
        doska = [list(i) for i in doska]
    for a in range(1, 4):

        #  просчитывание клеток под боем для нижней части ходов фигуры
        if 0 <= i + a < N:
            c = j - a
            for b in range(3):
                if 0 <= c < N:
                    doska[i + a][c] = '*'
                c += a

        # просчитывание клеток под боем для верхнй части ходов фигуры
        if 0 <= i - a < N:
            c = j - a
            for b in range(3):
                if 0 <= c < N:
                    doska[i - a][c] = '*'
                c += a

        # просчитывание клеток под боем по горизонтали
        if 0 <= j - a < N:
            doska[i][j - a] = '*'

        if 0 <= j + a < N:
            doska[i][j + a] = '*'

    if not flag:
        doska = [tuple(i) for i in doska]
    return doska


def vyvod_doski_v_konsol(doska):
    doska = [list(i) for i in doska]
    for stroka in doska:
        stroka = ' '.join([str(i) for i in stroka])
        print(stroka)


L = 0
N = 0
console_doska = False
kolvo_otvet = 0
otvet = set()
if __name__ == '__main__':
    main()
