def main():
    cnt = 0
    for i in range(3):
        num = int(input('Введите число'))
        if num % 2 == 0:
            cnt += 1

    print("Четных чисел", cnt)
if __name__ == '__main__':
    main()