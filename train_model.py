import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

# Загрузка данных
X_train = pd.read_csv('data/X_train.csv')
y_train = pd.read_csv('data/y_train.csv')

# Создание и обучение модели
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Сохранение модели
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Модель успешно обучена и сохранена!")
