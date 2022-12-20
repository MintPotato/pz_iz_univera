def reccurs(a, num, otv):
    global abeba
    if num == s:
        abeba = otv
        return True
    elif a:
        if reccurs(a[1:], num + a[0], otv + '+') or reccurs(a[1:], num - a[0], otv + '-'):
            return True
    return False


a = list(map(int, input().split()))
s = -841
# s = a[-1]
b = a
abeba = ''
count = 0
for i in range(len(b)):

    if reccurs(b[i + 1:], b[i], ''):
        print(abeba)
    else:
        print('ns')
    # count += 1
    # print(reccurs(b[i + 1:], b[i], ''), abeba)

print(b)