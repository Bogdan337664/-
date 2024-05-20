import csv
with open('../данные.csv', mode='w', newline='', encoding='utf-8') as файл:
    писатель = csv.writer(файл)
    писатель.writerow(["Имя", "Отчество", "Возраст"])
    писатель.writerow(['Смирнов', "Алексей", 30])

def вывод_файла(имя_файла: str):
    with open(имя_файла, mode='r', newline='', encoding='utf-8') as файл:
        читатель = csv.reader(файл)
        for строка in читатель:
            print(', '.join(строка))

вывод_файла('../данные.csv')
