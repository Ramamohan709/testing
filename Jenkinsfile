pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Unit Tests') {
            steps {
                sh "python3 -m unittest discover -s app -p 'test_*.py' -v"
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-practice:${BUILD_NUMBER} .'
            }
        }
    }

    post {
        success {
            echo 'Tests passed and Docker image was built.'
        }
        failure {
            echo 'Pipeline failed. Review the stage logs.'
        }
    }
}
