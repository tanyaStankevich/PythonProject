# Задание 1
print("введите Х")
x = int(input())
print("введите Y")
y = int(input())
z = x + 1
count = 0
while x < z < y:
    if z % 2 == 0:
        print(z)
        z = z + 1
        count += 1
    elif z % 3 == 0:
        print(z)
        z = z + 1
        count += 1
    else:
        z = z + 1

print(count)

# Задание 2

print("Введите х")
count = int(input())
print("введите", count, "целых чисел")

a = [0] * count
i = 0
while count != 0:
    while i < count:
        b = int(input())
        a[i] = b
        print(a)
        i = i + 1
    count -= 1
b = max(a)
print('Первое максимальное из введенных чисел', b)
a.remove(b)
c = max(a)
print('Второе максимальное из введенных чисел', c)


# Задание 3
print("Введите желаемую зарплату")
salary = int(input())

if salary // 25:
    ost1 = salary % 25
    print("В вашей зарплате", salary // 25, "25 рублевых купюр")
    if ost1 // 10:
        ost2 = salary % 10
        print("В вашей зарплате", ost1 // 10, "10 рублевых купюр")
        if ost2 // 3:
            ost3 = salary % 3
            print("В вашей зарплате", ost2 // 3, "3 рублевых купюр")
            if ost3 // 1:
                print("В вашей зарплате", ost3 // 1, "1 рублевых купюр")

# Задание 4
print("Введите многозначное число")
a = input()
print(type(a))
b = list(a)
print(b)

i = 0
while i+1 < len(b):
    if b[i] < b[i + 1]:
        i = i + 1
    elif b[i] > b[i + 1]:
        print("Последовательность цифр этого числа не упорядочена")
exit()

print("Последовательность цифр числа упорядочена")
