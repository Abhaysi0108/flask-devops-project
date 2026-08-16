pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "abhaysingh07/flask-app:v1"
    }

    stages {

        stage('Code Clone') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login \
                        -u "$DOCKER_USER" \
                        --password-stdin
                    '''
                }
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $DOCKER_IMAGE'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker rm -f flask-container || true

                    docker run -d \
                        --name flask-container \
                        -p 5000:5000 \
                        $DOCKER_IMAGE
                '''
            }
        }
    }
}
