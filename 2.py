def main():
    num = int(input("Введите трехзначное число"))
    num1 = num // 100
    num2 = num % 100 // 10
    num3 = num % 10
    if num1 == num2 or num1 == num3 or num2 == num3:
        print('Цифры в числе повторяются')
    else:
        print('Цифры в числе не повторяются')

if __name__ == '__main__':
    main()