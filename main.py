'''
myfile = open("vocabulary.csv", "a")
myfile.write("test2;тест2\n")
myfile.close()
'''

import csv

FILENAME = "users.csv"

users = [
    {"word": "test", "translate": "тест"},
    {"word": "word", "translate": "слово"}
]

with open(FILENAME, "w", newline="") as file:
    columns = ["word", "translate"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()

    # запись нескольких строк
    writer.writerows(users)

    user = {"word": "Sam", "translate": "Сэм"}
    # запись одной строки
    writer.writerow(user)

with open(FILENAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["word"], "-", row["translate"])