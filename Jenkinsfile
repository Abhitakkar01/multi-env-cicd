pipeline {
    agent any

    stages {
        stage('DEV') {
            steps {
                bat 'echo DEV stage started'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t multi-env-app:latest .'
            }
        }

        stage('QA') {
            steps {
                bat 'docker images'
            }
        }

        stage('PROD') {
            steps {
                bat 'echo PROD deployment placeholder'
            }
        }
    }
}
