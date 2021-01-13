import csv
import random
import datetime


def new_time(particular_time):  # новая дата для слова
    with open("test.csv", "r") as file:  # 1. читаем все строки в файле
        lines = file.readlines()
    for line in lines:  # 2. удаляем строку пройденного слова (определяем по времени)
        if oldest_records[count][2] in line:
            lines.remove(line)
    with open("test.csv", "w") as file:  # 3. записываем обратно все строки без убранной
        file.writelines(lines)
    with open("test.csv", mode="a", encoding='utf-8') as w_file:  # 4. дописываем в конец файла слово с новой датой
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        oldest_records[count][2] = particular_time
        file_writer.writerow(oldest_records[count])


def training():
    with open("test.csv", encoding='utf-8') as r_file:  # открываем файл на чтение
        reader = csv.reader(r_file, delimiter=",")
        sortedlist = sorted(reader, key=lambda row: row[2], reverse=False)  # сортировка по дате
        oldest_records = sortedlist[0:3]  # выбор трех самых старых записей
        for i in range(3):  # цикл для взаимодействия с пользователем (вопрос-ответ)
            answer_list = []  # обнуляем список вариантов ответа
            count = random.randint(0, len(oldest_records) - 1)  # для рандома
            print(oldest_records[count][0])  # выводим слово-вопрос
            answer_list.append(oldest_records[count][1])  # добавляем правильный ответ к списку вариантов
            with open("test.csv", encoding='utf-8') as r_file1:  # считаем кол-во строк в файле
                reader1 = csv.reader(r_file1, delimiter=",")
                strok_vsego = 0
                for m in reader1:
                    strok_vsego += 1
            rand_spis = []
            for nn in range(4):  # выбираем номера строк для случайных вариантов ответа
                rand_spis.append(random.randint(1, strok_vsego))
            # print(rand_spis)  # какие элементы тащит для вариантов ответа
            with open("test.csv", encoding='utf-8') as r_file2:  # выбираем случайные варианты ответа по известным номерам
                reader2 = csv.reader(r_file2, delimiter=",")
                nomer_stroki = 0
                for n in reader2:
                    nomer_stroki += 1
                    if nomer_stroki in rand_spis:
                        answer_list.append(n[1])
            random.shuffle(answer_list)  # перемешиваем список вариантов ответа
            print('---select right answer (0 для выхода)---')  # показываем варианты пользователю
            counter = 0
            for x in answer_list:
                counter += 1
                print(counter, x)
            answer1 = int(input())  # спрашиваем номер правильного варианта
            if answer1 == 0:
                main_menu()
            if answer_list[answer1 - 1] == oldest_records[count][1]:  # условие если правильно/неправильно
                print('great!')
                now = datetime.datetime.now()
                new_time(str(now.isoformat()))
            else:
                print(f'nope, right answer is: {oldest_records[count][1].lower()}')
                tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
                new_time(str(tomorrow.isoformat()))
            del(oldest_records[count])  # слово пройдено, убираем из цикла


def new_word():
    class NewWord:
        word = input('введите новое слово: ')
        translate = input('введите перевод: ')
        print('все верно?', word, '-', translate)
        answer = input()
        if answer == '+':
            pass
        elif answer == '-':
            new_word()


def main_menu():
    print('''лео сосатб
----------
выбери действие:
[1] тренироваться
[2] добавить слово

[0] выход''')
    action = int(input())
    if action == 0:
        exit()
    elif action == 1:
        training()
    elif action == 2:
        new_word()


main_menu()
