pipeline {
    agent {
        docker { image 'python:3.9-slim' }
    }
    stages {
        stage('Setup') {
            steps {
                sh 'pip install pandas scikit-learn joblib'
            }
        }
        stage('Fetch Data') {
            steps {
                sh 'wget https://example.com/data.csv'
            }
        }
        stage('Prepare Data') {
            steps {
                sh 'python data_preparation.py'
            }
        }
        stage('Train Model') {
            steps {
                sh 'python model_training.py'
            }
        }
        stage('Evaluate Model') {
            steps {
                sh 'python model_evaluation.py'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '*.pkl, *.csv', fingerprint: true
        }
    }
}
