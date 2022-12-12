import random

list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
list2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

z = 0
w = 0
list3 = []
list = []

i = 0
j = 0
win1 = 0
win2 = 0
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

listplayer = []

# Функция генерации кораблей
def place(dl, count):
    cop = dl
    while count > 0:
        k = random.randint(0, 9)
        m = random.randint(0, 9)
        coord = list[k][m]
        listplayer.append(coord)

        while dl > 1:
            k = k - 1

            listplayer.append(list[k][m])
            dl -= 1
        if dl == 1:
            count -= 1
            dl = cop

    if count == 0:
        return listplayer

#Генерируем корабли 1 игрока

place(4, 1)
# place(3, 2)
# place(2, 3)
# place(1, 4)
listplayer1 = []
listplayer1 = listplayer.copy()
print(listplayer1)

#Генерируем корабли 2 игрока

listplayer.clear()
place(4, 1)
# place(3, 2)
# place(2, 3)
# place(1, 4)
listplayer2 = []
listplayer2 = listplayer.copy()
print(listplayer2)

# Игрок 1 начинает игру
a1 = 0
a2 = 0

# while listplayer1 != 0 and listplayer2 != 0:
while a1 == 0 and len(listplayer2) > 0 and win2 !=1:
    l2 = len(listplayer2)
    b1 = 0
    print('Игрок 1, введите координату')
    h1 = poisk(input())
    for i in listplayer2:
        if h1 == i:
            listplayer2.remove(i)
            print('Вы попали, у вас еще один ход')
            print(len(listplayer2))
            b1 = 1
        if h1 != i:
            l2 -= 1
        if h1 != i and l2 == 1:
            a1 = 1
            print('Мимо')
    if len(listplayer2) == 0:
        win1 = 1
        print('Игрок1 вы победили')


while a2 == 0 and len(listplayer1) > 0 and win1 != 1:
    l1 = len(listplayer1)
    b2 = 0
    print('Игрок 2, введите координату')
    h2 = poisk(input())

    for i in listplayer1:

        if h2 == i:
            listplayer1.remove(i)
            print('Вы попали, у вас еще один ход')
            print(len(listplayer1))
            b2 = 1
        if h2 != i:
            l1 -= 1
        if h2 != i and l1 == 1:
            a2 = 1
            print('Мимо')
    if len(listplayer1) == 0:
        win2 = 1
        print('Игрок2 вы победили')







