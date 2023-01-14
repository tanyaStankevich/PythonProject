import random

# Задание 1
a = [1, 15, 17, 9, 21, 35]
b = 0
i = 0
while i < len(a):
    if i % 2 == 0:
        b = b + a[i]
    i = i + 1
print(b)




# Задание 2
print('Введите количество элементов в массиве по горизонтали')
b = int(input())
print('Введите количество элементов в массиве по вертикали')
a = int(input())
mas = [0]*a
i = 0
s = 0

for i in range(a):
    mas[i] = [0]*b
print(mas)

for i in range(b):
    for j in range(a):
        mas[j][i] = random.randint(0, 100)

print(mas)

for i in range(a):
    for j in range(b):

        s = s + mas[i][j]
    print(s)
    s = 0



# Задание 3
l = [0]*30
y = 1
i = 0
while i < 30:
     l[i] = random.randint(0, 100)
     i = i + 1
print(l)


for i in range(len(l)):
    for y in range(i+1, len(l)):
        if l[i] > l[y]:
            l[i], l[y] = l[y], l[i]


print(l)