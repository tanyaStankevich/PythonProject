# Задание 1

print("Узнайте какой день выходной. Введите день недели цифрой: где 1 понедельник, 7 - воскресенье")
i = 0
while i < 100:
    a = int(input())
    if a == 6 or a == 7:
        print('-', {a}, '->', 'да')
        i = i + 1
    elif 0 < a < 6:
        print('-', {a}, '->', 'нет')
        i = i + 1
    else:
        print('Значение не соответствует цифре дня недели')
        i = i + 1

# Задание 2
print("Введите x")
x = int(input())
print("Введите y")
y = int(input())
print("Введите z")
z = int(input())

left = not (x or y or z)
right = not x and not y and not z
if left == right:
    print('Выражение ошибочно')
else:
    print('Выражение истинно')

# Задание 3
i = 0
while i < 100:
    print("Введите координату x")
    x = int(input())
    print("Введите координату y")
    y = int(input())

    if x > 0 and y > 0:
        print("x=", x, "y=", y, "-> 1")
        i = i + 1
    elif x > 0 and y < 0:
        print("x=", x, "y=", y, "-> 4")
        i = i + 1
    elif x < 0 and y < 0:
        print("x=", x, "y=", y, "-> 3")
        i = i + 1
    elif x < 0 and y > 0:
        print("x=", x, "y=", y, "-> 2")
        i = i + 1
    elif x == 0 and y == 0:
        print('x и y не должны быть равны 0')
        i = i + 1

# Задание 4
i = 0
while i < 10:
    print("Введите номер четверти оси координат (1, 2, 3, 4)")
    x = int(input())

    if x == 1:
        print(x, "четверть", "диапазон координат х (0;100), диапазон координат у (0;100)")
        i = i + 1
    elif x == 2:
        print(x, "четверть", "диапазон координат х (0;-100), диапазон координат у (0;100)")
        i = i + 1
    elif x == 3:
        print(x, "четверть", "диапазон координат х (0;-100), диапазон координат у (0;-100)")
        i = i + 1
    elif x == 4:
        print(x, "четверть", "диапазон координат х (0;100), диапазон координат у (0;-100)")
        i = i + 1
    else:
        print('Выберите 1, 2, 3, 4 четверть')
        i = i + 1

# Задание 5
i = 0
while i < 100:
    print('Введите координаты первой точки A')
    print('Введите x')
    ax = int(input())
    print('Введите y')
    ay = int(input())

    print('Введите координаты второй точки В')
    print('Введите x')
    bx = int(input())
    print('Введите y')
    by = int(input())
    r = ((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5

    print("- A (", ax, ";", ay, "); B(", bx, ";", by, ") ->", {r})
    i = i + 1