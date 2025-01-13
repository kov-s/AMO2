pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/kov-s/AMO2/'
            }
        }
        stage('Build') {
            agent {
                docker {
                    image 'python:3.9-slim'
                }
            }
            steps {
                sh 'docker inspect -f . python:3.9-slim'
                sh 'docker pull python:3.9-slim'
            }
        }
    }
}
