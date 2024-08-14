pipeline {
    agent any
    environment {
        IMAGE_NAME = 'wog-docker'
        IMAGE_TAG = 'latest'
        DOCKER_CREDENTIALS_ID = 'docker-hub-credential'
    }
    stages {
        stage('Clean UP') {
            steps {
                deleteDir()
            }
        }
        stage('Clone Repo') {
            steps {
                bat "git clone https://github.com/Mapti94/Matan_Ptito-WOG-0105.git ."
            }
        }
        stage('List Directory') {
            steps {
                bat "dir"
            }
        }
        stage('Docker') {
            steps {
                script {
                    // Run docker-compose command in the current directory
                    bat "docker-compose up --build -d"
                }
            }
        }
        stage('E2E') {
            steps {
                // Run e2e tests in the current directory
                bat "python e2e.py"
            }
        }
        stage('Finalize') {
            steps {
                // Run docker-compose down in the current directory
                bat "docker-compose down"
            }
        }
        stage('Docker Login') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: env.DOCKER_CREDENTIALS_ID, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        bat "docker login -u %DOCKER_USER% -p %DOCKER_PASS%"
                    }
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    bat "docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:${IMAGE_TAG}"
                    bat "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }
    }
}
