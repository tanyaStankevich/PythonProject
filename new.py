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