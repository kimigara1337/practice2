import pandas as pd
import json
import msgpack
import pickle
import os

# Загружаем набор данных из CSV файла
iris_df = pd.read_csv(r"E:\66\lab2\66\iris.csv")

# Выбираем 5 полей для анализа
selected_fields = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"]
filtered_iris_df = iris_df[selected_fields].copy()

# Расчет характеристик для числовых полей
stats = {}
numeric_fields = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]

for field in numeric_fields:
    stats[field] = {
        "max": filtered_iris_df[field].max(),
        "min": filtered_iris_df[field].min(),
        "mean": filtered_iris_df[field].mean(),
        "sum": filtered_iris_df[field].sum(),
        "std": filtered_iris_df[field].std(),
    }

# Подсчет частоты встречаемости для текстового поля
categorical_fields = ["Species"]
for field in categorical_fields:
    stats[field] = filtered_iris_df[field].value_counts().to_dict()

# Сохранение расчетов в JSON формате
with open("iris_statistics.json", "w", encoding="utf-8") as f:
    json.dump(stats, f, ensure_ascii=False, indent=4)

# Сохранение обрезанных данных в различных форматах
# CSV
filtered_iris_df.to_csv("filtered_iris.csv", index=False)

# JSON
with open("filtered_iris.json", "w", encoding="utf-8") as f:
    json.dump(filtered_iris_df.to_dict(orient='records'), f, ensure_ascii=False, indent=4)

# MsgPack
with open("filtered_iris.msgpack", "wb") as f:
    msgpack.dump(filtered_iris_df.to_dict(orient='records'), f)

# Pickle
with open("filtered_iris.pkl", "wb") as f:
    pickle.dump(filtered_iris_df, f)

# Сравнение размеров полученных файлов
csv_size = os.path.getsize("filtered_iris.csv")
json_size = os.path.getsize("filtered_iris.json")
msgpack_size = os.path.getsize("filtered_iris.msgpack")
pickle_size = os.path.getsize("filtered_iris.pkl")

print(f"Размер CSV файла: {csv_size} байт")
print(f"Размер JSON файла: {json_size} байт")
print(f"Размер MsgPack файла: {msgpack_size} байт")
print(f"Размер Pickle файла: {pickle_size} байт")
