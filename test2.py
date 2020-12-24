import csv
import random
import datetime

print('test server_side2')

with open("test.csv", encoding='utf-8') as r_file:
    reader = csv.reader(r_file, delimiter=";")
    sortedlist = sorted(reader, key=lambda row: row[2], reverse=False)
    oldest_records = sortedlist[0:3]
    for i in range(3):
        count = random.randint(0, len(oldest_records) - 1)
        print(oldest_records[count][0])
        answer = input("answer: ")
        if answer == oldest_records[count][1]:
            now = datetime.datetime.now()
            print('great!')
            with open("test.csv", "r") as file:
                lines = file.readlines()
            for line in lines:
                if oldest_records[count][2] in line:
                    lines.remove(line)
            with open("test.csv", "w") as file:
                file.writelines(lines)
            with open("test.csv", mode="a", encoding='utf-8') as w_file:
                file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
                oldest_records[count][2] = now.isoformat()
                file_writer.writerow(oldest_records[count])
        else:
            print('nope..')
            print('yeeet')
        del(oldest_records[count])
