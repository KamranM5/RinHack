import pandas as pd
import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense
from analyse import *



# Загрузка модели
model = Sequential()
model = load_model("model.h5") 

# Предсказание для новых данных
new_data = pd.read_csv("for_test.csv", delimiter="|")
X_new = np.array(new_data.iloc[:, :])  # Входные параметры новых данных
predictions = model.predict(X_new)  # Предсказание для новых данных

# Сохранение результатов в файл
results = pd.DataFrame(predictions)  # Создаем DataFrame с предсказаниями
results.to_csv("test_results.csv", index=False, sep="|")  # Сохраняем результаты в csv файл

analyse("results.csv", "result.csv")
