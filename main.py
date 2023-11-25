import pandas as pd
import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense

# Чтение данных из csv файла
data = pd.read_csv("full.csv", delimiter="|")
X = np.array(data.iloc[:, :-1])  # Входные параметры (первые 14 столбцов)
y = np.array(data.iloc[:, -1])  # Выходной параметр (последний столбец)

# Создание модели нейронной сети
model = Sequential()
model.add(Dense(64, input_dim=13, activation='relu'))  # Полносвязный слой с 64 нейронами и функцией активации ReLU
model.add(Dense(1))  # Выходной слой с одним нейроном (прогнозируемый параметр)

# Компиляция модели
model.compile(loss='mse', optimizer='adam')  # Используем среднеквадратичную ошибку (MSE) в качестве функции потерь и алгоритм оптимизации Adam

# Обучение модели
model.fit(X, y, epochs=850, batch_size=32)  # Обучение модели на входных и выходных данных для 850 эпох с размером пакета 32

# Сохранение модели
model.save("model.h5")

# Загрузка модели
model = Sequential()
model = load_model("model.h5") 

# Рассчет для новых данных
new_data = pd.read_csv("for_test.csv", delimiter="|")
X_new = np.array(new_data.iloc[:, :])  # Входные параметры новых данных
predictions = model.predict(X_new)  # Предсказание для новых данных

# Сохранение результатов в файл
results = pd.DataFrame(predictions, columns=["Параметр_15"])  # Создаем DataFrame с предсказаниями
results.to_csv("test_results.csv", index=False, sep="|")  # Сохраняем результаты в csv файл
