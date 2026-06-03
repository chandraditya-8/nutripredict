pipeline {
    agent any
    environment {
        IMAGE_NAME = "chandraditya9090/nutripredict"
    }
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }
        stage('Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }
        stage('Push') {
            steps {
                sh 'docker push $IMAGE_NAME:latest'
            }
        }
    }
}
