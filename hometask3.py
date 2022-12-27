# Задание 1

print('Введите десятичное число')
ten = int(input())
y = []
x = 100
while x != 0:
    z = ten // 16
    x = ten % 16
    ten = z
    if x == 10:
        x = 'A'
        y.append(x)

    elif x == 11:
        x = 'B'
        y.append(x)

    elif x == 12:
        x = 'C'
        y.append(x)

    elif x == 13:
        x = 'D'
        y.append(x)

    elif x == 14:
        x = 'E'
        y.append(x)

    elif x == 15:
        x = 'F'
        y.append(x)

    else:
        y.append(str(x))

    if z == 0:
        y = ''.join(map(str, y))
        y = y[::-1]
        print(y)
        exit()

# Задание 2
print('Введите строку')
a = input()

if a.isnumeric() == False:
    print("Введенная строка не является дробью")
else:
    print("Введенная строка является дробью")

# Задание 3

print('Введите строку')
a = list(input())

print(a)
i = 0
b = [0]*len(a)
c = [0]*len(a)
d = [0]*len(a)
rev = [0]*len(a)
count = 0

while i < len(a):
    b[i] = a[i]


    if b[i] == 'o':
        print(b)
        i = i + 1

        while i < len(a):

            if a[i] == 'o':
                d[i] = a[i]
                print(c)
                i = i + 1

                while i < len(a):
                    d[i] = a[i]
                    i = i + 1
                print(d)
                c = c[::-1]
                print(c)

                i = 0
                while i < len(rev):
                    rev[i] = b[i]
                    if b[i] == 0:
                        while i < len(rev):
                            rev[i] = c[i]
                            i = i + 1
                            if c[i] == 0:
                                while i < len(rev):
                                    rev[i] = d[i]
                                    i = i + 1
                                print(''.join(map(str, rev)))
                                exit()
                    i = i + 1


            else:
                c[i] = a[i]

            i = i + 1

    i = i + 1

while i < len(a):

    if a[i] == 'o':
        i = i + 1
        count += 1
    i = i + 1
if count < 2:
    print("Фраза содержит менее 2 'o'")
    exit()





