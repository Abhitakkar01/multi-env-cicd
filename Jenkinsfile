pipeline {
    agent any

    stages {
        stage('DEV') {
            steps {
                bat 'echo Deploying to DEV environment'
                bat 'dir'
            }
        }

        stage('QA') {
            steps {
                bat 'echo Testing in QA environment'
            }
        }

        stage('PROD') {
            steps {
                bat 'echo Deploying to PROD environment'
            }
        }
    }
}
