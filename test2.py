import csv
import random
import datetime


def new_time(particular_time):
    with open("test.csv", "r") as file:
        lines = file.readlines()
    for line in lines:
        if oldest_records[count][2] in line:
            lines.remove(line)
    with open("test.csv", "w") as file:
        file.writelines(lines)
    with open("test.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        oldest_records[count][2] = particular_time
        file_writer.writerow(oldest_records[count])


with open("test.csv", encoding='utf-8') as r_file:
    reader = csv.reader(r_file, delimiter=",")
    sortedlist = sorted(reader, key=lambda row: row[2], reverse=False)
    oldest_records = sortedlist[0:3]
    answer_list = []
    for i in range(3):
        count = random.randint(0, len(oldest_records) - 1)
        print(oldest_records[count][0])
        answer_list.append(oldest_records[count][1])
        with open("test.csv", encoding='utf-8') as r_file1:
            reader1 = csv.reader(r_file1, delimiter=",")
            strok_vsego = 0
            for m in reader1:
                strok_vsego += 1
        rand_spis = []  # надо добить, чтобы цикл срабатывал верно при 2 и более итерациях
        for nn in range(4):
            rand_spis.append(random.randint(1, strok_vsego))
        # print(rand_spis)  # какие элементы тащит для вариантов ответа
        with open("test.csv", encoding='utf-8') as r_file2:
            reader2 = csv.reader(r_file2, delimiter=",")
            nomer_stroki = 0
            for n in reader2:
                nomer_stroki += 1
                if nomer_stroki in rand_spis:
                    answer_list.append(n[1])
            random.shuffle(answer_list)
            print('select right answer:', answer_list)
            answer1 = int(input())
            if answer_list[answer1 - 1] == oldest_records[count][1]:
                print('great!')
                now = datetime.datetime.now()
                new_time(str(now.isoformat()))
            else:
                print(f'nope, right answer is: {oldest_records[count][1].lower()}')
                tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
                new_time(str(tomorrow.isoformat()))
            del(oldest_records[count])
