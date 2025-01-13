pipeline {
    agent {
        docker {
            image 'python:3.9-slim' // Используем Python внутри Docker
        }
    }
    stages {
        stage('Setup') {
            steps {
                sh '''
                apt-get update && apt-get install -y wget git
                pip install -U pip
                pip install pandas scikit-learn joblib
                '''
            }
        }
        stage('Data Fetching') {
            steps {
                sh '''
                # Скачиваем данные
                git clone https://github.com/ваш_репозиторий_с_данными.git data_repo
                cp data_repo/data.csv .
                '''
            }
        }
        stage('Data Preparation') {
            steps {
                script {
                    writeFile file: 'data_preparation.py', text: '''
import pandas as pd
from sklearn.model_selection import train_test_split

# Загрузка данных
data = pd.read_csv("data.csv")

# Предобработка данных
data = data.dropna()  # Убираем пропуски
X = data[['feature1', 'feature2']]  # Важные признаки
y = data['target']

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Сохраняем датасеты
X_train.to_csv('X_train.csv', index=False)
X_test.to_csv('X_test.csv', index=False)
y_train.to_csv('y_train.csv', index=False)
y_test.to_csv('y_test.csv', index=False)
'''
                }
                sh 'python data_preparation.py'
            }
        }
        stage('Model Training') {
            steps {
                script {
                    writeFile file: 'model_training.py', text: '''
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Загрузка данных
X_train = pd.read_csv('X_train.csv')
y_train = pd.read_csv('y_train.csv')

# Создание модели
model = RandomForestClassifier()
model.fit(X_train, y_train.values.ravel())

# Сохранение модели
joblib.dump(model, 'model.pkl')
'''
                }
                sh 'python model_training.py'
            }
        }
        stage('Model Evaluation') {
            steps {
                script {
                    writeFile file: 'model_evaluation.py', text: '''
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

# Загрузка данных
X_test = pd.read_csv('X_test.csv')
y_test = pd.read_csv('y_test.csv')

# Загрузка модели
model = joblib.load('model.pkl')

# Оценка модели
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
'''
                }
                sh 'python model_evaluation.py'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '*.pkl, *.csv', fingerprint: true
            junit '**/results.xml'  // Сохраняем артефакты
        }
    }
}
