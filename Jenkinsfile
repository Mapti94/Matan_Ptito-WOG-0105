pipeline {
    agent any
    environment {
        IMAGE_NAME = 'Mapti94/Matan_Ptito-WOG-0105'
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
                bat "git clone https://github.com/Mapti94/Matan_Ptito-WOG-0105.git"
            }
        }
        stage('Docker') {
            steps {
                script {
                    dir('WOG') {
                        bat "docker-compose up --build -d"
                    }
                }
            }
        }
        stage('E2E') {
            steps {
                dir('WOG') {
                    bat "python e2e.py"
                }
            }
        }
        stage('Finalize') {
            steps {
                dir('WOG') {
                    bat "docker-compose down"
                }
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