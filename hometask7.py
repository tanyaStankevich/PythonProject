
x = 0 # для бесконечного цикла
i = 1 # для нумирации строк в файле


def open_file(path,op): # функция открытия файла для чтения или записи
    schedule = open(path, op)
    line = schedule.readline()

    while line:
        print(line)
        line = schedule.readline()

    schedule.close()


# Запускаем бесконечный цикл
while x == 0:
    print('Что вы хотите сделать (выберите цифру): 0 - просмотреть записи, 1 - добавить запись, 2 - удалить запись, 3 - изменить существующую '
          'запись')
    a = int(input())

    if a == 0:
        open_file('sched.txt', 'r')

    if a == 1:
        print('Введите запись')
        schedule = open('sched.txt', 'a')
        i = str(i)
        schedule.write(i +' ' + input() + '\n')
        i = int(i)
        i += 1
        schedule.close()


    if a == 2:
        open_file('sched.txt', 'r')

        print('Выберите номер записи, которую нужно удалить')
        delete = input()
        schedule = open('sched.txt', 'r')
        schedule_write = open('sched2.txt', 'w')
        line = schedule.readline()
        # schedule_write.write(line)

        while line:

            j = 1
            for j in range(len(line)):
                if line[0] == delete:

                    schedule_write.write('')
                    break
                if line[0] != delete:
                    schedule_write.write(line)
                    break
            line = schedule.readline()

        schedule.close()
        schedule_write.close()
        schedule = open('sched.txt', 'w')
        schedule_write = open('sched2.txt', 'r')


        linecopy = schedule_write.readline()
        while linecopy and linecopy !='':
            schedule.write(linecopy)
            linecopy = schedule_write.readline()
        schedule.close()
        schedule_write.close()


    if a ==3:
        open_file('sched.txt', 'r')

        print('Выберите номер записи, которую нужно изменить')
        change = input()
        schedule = open('sched.txt', 'r')
        schedule_write = open('sched2.txt', 'w')
        line = schedule.readline()
        # schedule_write.write(line)

        print('Введите измененную запись')
        while line:

            j = 1
            for j in range(len(line)):
                if line[0] == change:
                    schedule_write.write(change + ' ' + input())
                    break
                if line[0] != change:
                    schedule_write.write(line)
                    break
            line = schedule.readline()

        schedule.close()
        schedule_write.close()
        schedule = open('sched.txt', 'w')
        schedule_write = open('sched2.txt', 'r')

        linecopy = schedule_write.readline()
        while linecopy and linecopy != '':
            schedule.write(linecopy)
            linecopy = schedule_write.readline()
        schedule.close()
        schedule_write.close()