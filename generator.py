import random

with open("generator.csv", "w") as file:
    for index in range(10):
        file.write(str(random.randint(100000, 999999)) + '\n')
