import pickle
from sklearn.metrics import accuracy_score
import pandas as pd

# Загрузка данных
X_test = pd.read_csv('data/X_test.csv')
y_test = pd.read_csv('data/y_test.csv').squeeze()

# Загрузка сохранённой модели
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Предсказание на тестовых данных
y_pred = model.predict(X_test)

# Оценка качества модели
accuracy = accuracy_score(y_test, y_pred)
print(f"Точность модели на тестовых данных: {accuracy:.2f}")
