def main():
    num1 = int(input("Введите число №1"))
    num2 = int(input("Введите число №2"))
    num3 = int(input("Введите число №3"))

    cnt = 0    
    if num1 == num2:
        cnt +=2
        if num1 == num3:
            cnt += 1
    elif num2 == num3:
        cnt += 2
    elif num1 == num3:
        cnt += 2
    
    print(cnt)


if __name__ == '__main__':
    main()