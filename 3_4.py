import pandas as pd

def объединить_csv_файлы(входные_файлы: list[str], выходной_файл: str):
    список_датафреймов = []
    for файл in входные_файлы:
        датафрейм = pd.read_csv(файл)
        список_датафреймов.append(датафрейм)
    объединенный_датафрейм = pd.concat(список_датафреймов, ignore_index=True)
    объединенный_датафрейм.to_csv(выходной_файл, index=False)

первый_csv_файл = "./один.csv"
второй_csv_файл = "./два.csv"
объединить_csv_файлы(входные_файлы=[первый_csv_файл, второй_csv_файл], выходной_файл="./результат.csv")
