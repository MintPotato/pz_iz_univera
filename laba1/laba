def recurs(spisok_chisel: list, chislo: int, otv: str, s: int) -> bool:
    global g_otv

    """Если число найдено, то Записываем порядок знаков в g_otv"""
    if not spisok_chisel:
        if chislo == s:
            g_otv = otv
            return True
        else:
            return False

    """Если число было найдено, возвращаем истину"""
    if recurs(spisok_chisel[1:], chislo + spisok_chisel[0], otv + '+', s) or \
            recurs(spisok_chisel[1:], chislo - spisok_chisel[0], otv + '-', s):
        return True

    return False  # иначе ложь


def krasiviy_vyvod(chisla: list, znaki: str, s: int, n: int) -> str:
    otv = str(chisla[0])

    for i in range(1, n):
        otv += znaki[i - 1] + str(chisla[i])

    otv += '=' + str(s)
    return otv


def main():
    """Чтение файла
    запись его значений в отдельный список
    Закрытие файла"""

    f = open('Имя файла', 'r+')
    a = list(map(int, list(f)[0].split()))

    """Перенос значений из полученного выше списка, в отдельные переменные, где n - количество чисел, 
    s - искомое число и chisla - список введенных чисел"""
    n = a[0]
    s = a[-1]
    chisla = a[1:-1]

    """Вызов рекурентной функции для составления всевозможных комбинаций знаков и проверка на присутстыие решения"""
    if recurs(chisla[1:], chisla[0], '', s):
        f.write('\n' + krasiviy_vyvod(chisla, g_otv, s,
                                      n))  # Если решение есть, то вызывается функция делающаяя необходимый вывод
        f.close()
    else:
        f.write('\n ns')  # Иначе - no solution
        f.close()


g_otv = ''
if __name__ == '__main__':
    main()
