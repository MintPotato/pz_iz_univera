def main():
    x = int(input("Введите координату х "))
    y = int(input("Введите координату у "))

    if x > 0:
        if y  > 0:
            print("Точка находиться в I четверти")
        else:
            print("Точка назодиться в IV четверти")
    else:
        if y > 0:
            print("Точка находиться во II четверти")
        else:
            print("Точка находиться в III четверти")


if __name__ == '__main__':
    main()
