import array
import csv
from Table import Table

table_list: array = []

def check_table():
    if table_list:
        return True
    else:
        print("Нет таблицы.")
        return False

def save():
    with open('table.csv', 'w+') as csv_file:
        fieldnames = ['name', "dept", 'role']

        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='\t')

        for table in table_list:
            csv_writer.writerow(table.get_dict())


def load():
    try:
        with open('table.csv', 'r') as csv_file:
            fieldnames = ['name', "dept", 'role']
            csv_reader = csv.DictReader(csv_file,fieldnames=fieldnames, delimiter='\t')

            for table in csv_reader:
                table_list.append(Table(table['name'], table['dept'], table['role']))
    except FileNotFoundError:
        pass

# если файл есть, загрузить
load()

while True:
    choice = int(input('''
    1. Добавить таблицу
    2. Изменить таблицу
    3. Удалить таблицу
    4. Распечатать таблицу преподавателей
    5. Распечатать таблицу кафедр
    6. Выход
    '''))

    if choice == 1:
        new_tab: Table = Table(input("Введите ФИО: "), input("Введите кафедру: "), input("Введите должность: "))
        print("Добавлено: " + str(new_tab))
        table_list.append(new_tab)

    if choice == 2: # изменение
        if check_table():
            edit_choice: int = (int(input("Введите номер таблицы: ")))

    if choice == 3: # удаление
        if check_table():
            table_list.pop(int(input("Введите номер таблицы: ")))

    if choice == 4: # таблица преподов
        if check_table():
            for i in table_list:
                print("(%s) " % table_list.index(i) + str(i))

    if choice == 5: # таблица кафедр
        if check_table():
            # создание набора уникальных кафедр
            depts = []
            for i in table_list:
                depts.append(i.dept)
            depts = set(depts)
            # группировка по кафедрам
            for i in depts:
                print("--%s--" % i)
                amount = 0
                for j in table_list:
                    if i == j.dept:
                        print("(%s) " % table_list.index(j) + str(j))
                        amount += 1
                print ("В кафедре %s %s преподавателей" % (i, amount))

    if choice == 6: # выход
        save()
        break
