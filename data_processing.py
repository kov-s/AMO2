import pandas as pd
from sklearn.model_selection import train_test_split


data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv" 
data = pd.read_csv(data_url)

# Предварительная обработка данных
# Удалим строки с пропущенными значениями (если есть)
data.dropna(inplace=True)

# Разделение на признаки и целевую переменную
X = data.drop(columns=['species'])  
y = data['species']

# Разделение на тренировочный и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Сохранение обработанных данных
X_train.to_csv('data/X_train.csv', index=False)
X_test.to_csv('data/X_test.csv', index=False)
y_train.to_csv('data/y_train.csv', index=False)
y_test.to_csv('data/y_test.csv', index=False)

print("Данные успешно обработаны и сохранены!")
