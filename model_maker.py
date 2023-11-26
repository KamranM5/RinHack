import pandas as pd
import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense

# Чтение данных из csv файла
data = pd.read_csv("training.csv", delimiter="|")
X = np.array(data.iloc[:, :-1])  # Входные параметры (первые 14 столбцов)
y = np.array(data.iloc[:, -1])  # Выходной параметр (последний столбец)

# Создание модели нейронной сети
model = Sequential()
model.add(Dense(64, input_dim=13, activation='relu'))  # Полносвязный слой с 64 нейронами и функцией активации ReLU
model.add(Dense(1))  # Выходной слой с одним нейроном (прогнозируемый параметр)

# Компиляция модели
model.compile(loss='mse', optimizer='adam')  # Используем среднеквадратичную ошибку (MSE) в качестве функции потерь и алгоритм оптимизации Adam

# Обучение модели
model.fit(X, y, epochs=2, batch_size=32)  # Обучение модели на входных и выходных данных для 2 эпох с размером пакета 32

# Сохранение модели
model.save("model.h5")
