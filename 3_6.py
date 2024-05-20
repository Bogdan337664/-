import pandas as pd
import glob
import os

def объединить_csv(директория):
    шаблон = os.path.join(директория, '*.csv')
    файлы = glob.glob(шаблон)
    датафреймы = []
    for файл in файлы:
        данные = pd.read_csv(файл)
        датафреймы.append(данные)
    if not датафреймы:
        print("Нет файлов для обработки.")
        return pd.DataFrame()
    объединенные_данные = датафреймы[0]
    for д in датафреймы[1:]:
        объединенные_данные = pd.merge(объединенные_данные, д, on='user_id', how='outer')
    return объединенные_данные
  
путь = './данные/'
объединенные_данные = объединить_csv(путь)
print(объединенные_данные.to_string())
