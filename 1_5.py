import csv
total_sum = 0
with open('C:/Users/levko/PycharmProjects/1/example_1kb.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        for cell in row:
            values = cell.split(',')
            for value in values:
                total_sum += int(value)
            print(total_sum / len(values))
