list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
list2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

z = 0
w = 0
list3 = []
list = []

i = 0
j = 0

# создание игрового поля
while i < len(list2):
    while j < len(list1):
        a = list2[i] + list1[j]
        list3.append(a)
        list4 = list3.copy()
        j += 1
    list.append(list4)
    list3.clear()
    j = 0
    i += 1
print(list)


# Функция проверки, что координата лежит в игровом поле
def poisk(l):
    k = 0
    m = 0
    for k in range(len(list)):
        for m in range(len(list)):
            if l == list[k][m]:
               return l
            elif l != list[k][m] and k == 9 and m == 9:
                print('Вы ввели несуществующую координату')
                poisk(input())


listplayer1 = []
# создание кораблей 1 игрока
print('Игрок 1: Введите координаты корабля из 4 клеток')

listplayer1.append(poisk(input()))
listplayer1.append(poisk(input()))
listplayer1.append(poisk(input()))
listplayer1.append(poisk(input()))

print('Игрок 1: Введите координаты 1 корабля из 3 клеток')
listplayer1.append(poisk(input()))
listplayer1.append(poisk(input()))
listplayer1.append(poisk(input()))

print('Игрок 1: Введите координаты 2 корабля из 3 клеток')
listplayer1.append(poisk(input()))
listplayer1.append(poisk(input()))
listplayer1.append(poisk(input()))

print('Игрок 1: Введите координаты 1 корабля из 2 клеток')
listplayer1.append(poisk(input()))
listplayer1.append(poisk(input()))

print('Игрок 1: Введите координаты 2 корабля из 2 клеток')
listplayer1.append(poisk(input()))
listplayer1.append(poisk(input()))

print('Игрок 1: Введите координаты 3 корабля из 2 клеток')
listplayer1.append(poisk(input()))
listplayer1.append(poisk(input()))

print('Игрок 1: Введите координаты 1 корабля из 1 клетки')
listplayer1.append(poisk(input()))

print('Игрок 1: Введите координаты 2 корабля из 1 клетки')
listplayer1.append(poisk(input()))
print('Игрок 1: Введите координаты 3 корабля из 1 клетки')
listplayer1.append(poisk(input()))
print('Игрок 1: Введите координаты 4 корабля из 1 клетки')
listplayer1.append(poisk(input()))
print(listplayer1)

listplayer2 = []
# создание кораблей 2 игрока
print('Игрок 2: Введите координаты корабля из 4 клеток')
listplayer2.append(poisk(input()))
listplayer2.append(poisk(input()))
listplayer2.append(poisk(input()))
listplayer2.append(poisk(input()))
print('Игрок 2: Введите координаты 1 корабля из 3 клеток')
listplayer2.append(poisk(input()))
listplayer2.append(poisk(input()))
listplayer2.append(poisk(input()))

print('Игрок 2: Введите координаты 2 корабля из 3 клеток')
listplayer2.append(poisk(input()))
listplayer2.append(poisk(input()))
listplayer2.append(poisk(input()))

print('Игрок 2: Введите координаты 1 корабля из 2 клеток')
listplayer2.append(poisk(input()))
listplayer2.append(poisk(input()))
print('Игрок 2: Введите координаты 2 корабля из 2 клеток')
listplayer2.append(poisk(input()))
listplayer2.append(poisk(input()))
print('Игрок 2: Введите координаты 3 корабля из 2 клеток')
listplayer2.append(poisk(input()))
listplayer2.append(poisk(input()))
print('Игрок 2: Введите координаты 1 корабля из 1 клетки')
listplayer2.append(poisk(input()))
print('Игрок 2: Введите координаты 2 корабля из 1 клетки')
listplayer2.append(poisk(input()))
print('Игрок 2: Введите координаты 3 корабля из 1 клетки')
listplayer2.append(poisk(input()))
print('Игрок 2: Введите координаты 4 корабля из 1 клетки')
listplayer2.append(poisk(input()))
print(listplayer2)

# Игрок 1 начинает игру
a1 = 0
a2 = 0



while listplayer1 != 0 and listplayer2 != 0:
    while a1 == 0:
        l2 = len(listplayer2)
        b1 = 0
        print('Игрок 1, введите координату')
        h1 = input()
        for z in range(len(list)):
            for j in range(len(list)):
                if h1 == list[j][z]:
                    for i in listplayer2:
                        if h1 == i:
                            listplayer2.remove(i)
                            print('Вы попали, у вас еще один ход')
                            b1 = 1
                        if h1 != i:
                            l2 -= 1
                        if h1 != i and l2 == 1:
                            a1 = 1
                            print('Мимо')

                if h1 != list[j][z] and j == 9 and z == 9 and a1 == 0 and b1 != 1:
                    print('Вы ввели несуществующую координату')

    while a2 == 0:
        l1 = len(listplayer1)
        b2 = 0
        print('Игрок 2, введите координату')
        h2 = input()
        for z in range(len(list)):
            for j in range(len(list)):
                if h2 == list[j][z]:
                    for i in listplayer1:

                        if h2 == i:
                            listplayer1.remove(i)
                            print('Вы попали, у вас еще один ход')
                            b2 = 1
                        if h2 != i:
                            l1 -= 1
                        if h2 != i and l1 == 1:
                            a2 = 1
                            print('Мимо')

                if h2 != list[j][z] and j == 9 and z == 9 and a2 == 0 and b2 != 1:
                    print('Вы ввели несуществующую координту')

    a1 = 0
    a2 = 0

if len(listplayer1) == 0:
    print('Игрок2 вы победили')

if len(listplayer2) == 0:
    print('Игрок1 вы победили')
