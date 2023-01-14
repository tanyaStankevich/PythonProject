
# Задание 1
class Soup():
    def __init__(self, name):
        self.name = name

    def add_soup(self):
        soup_write = open('soup.txt', 'a')
        print('Введите основной продукт супа ' + self.name)
        mainproduct = input()
        soup_write.write(self.name +'-' + mainproduct + '\n')
        soup_write.close()
    def show_soup(self, name):
        soup_read = open('soup.txt', 'r')
        line = soup_read.readline()

        while line and line !='':

            linelist = line.split('-')
            if linelist[0] == self.name:
                if linelist[1]=='\n':
                    print(linelist[0] + '-' + 'обычный кипяток')
                else:
                    print(linelist[0] + '-' + linelist[1])

            line = soup_read.readline()
        soup_read.close()




soup1 = Soup('Борщ')
soup1.add_soup()
soup2 = Soup('Гороховый')
soup2.add_soup()
soup3 = Soup('Щи')
soup3.add_soup()
soup1.show_soup('Борщ')
soup2.show_soup('Гороховый')
soup3.show_soup('Щи')

# Задание 2
class Student:
    def __init__(self, name, group, progress):
        self.name = name
        self.group = group
        self.progress = progress
    def sign(self):
        write_student = open('student.txt', 'a')
        write_student.write(self.name + '-' + self.group + '-' +self.progress + '\n')
        write_student.close()


def sort_name():
    read_student = open('student.txt', 'r')
    line = read_student.readline()
    list_sort_name = []

    while line and line !='':
        linelist = line.split('-')
        list_sort_name.append(linelist[0])
        line = read_student.readline()
    list_sort_name.sort()
    print(list_sort_name)
    read_student.close()

def sort_progress():
    read_student = open('student.txt', 'r')
    line = read_student.readline()
    list_sort_progress = []

    while line and line != '':
        linelist = line.split('-')
        a = int(linelist[2])
        if a <= 3:
            b = str(a)
            list_sort_progress.append(linelist[0] + ' ' + b)
        line = read_student.readline()
    print(list_sort_progress)

student1 = Student('Sidorov', 'KIB', '5')
student2 = Student('Ivanov', 'KIB', '3')
student3 = Student('Petrov', 'KIB', '4')
student4 = Student('Andropov', 'KIB', '2')
student1.sign()
student2.sign()
student3.sign()
student4.sign()
sort_name()
sort_progress()