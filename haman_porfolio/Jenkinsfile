pipeline {
    agent any

    environment {
        BACKEND_DIR = "portfolio/backend"
        FRONTEND_DIR = "portfolio/frontend"
        DOCKER_REGISTRY = "your-registry.hub.docker.com"
    }

    stages {
        stage("Checkout") {
            steps {
                checkout scm
            }
        }

        stage("Backend Tests") {
            steps {
                dir(env.BACKEND_DIR) {
                    script {
                        sh """
                            python3 -m venv venv
                            source venv/bin/activate
                            pip install -r requirements.txt
                            python -c "from app import create_app; app = create_app(); print('Backend imports successfully')"
                        """
                    }
                }
            }
        }

        stage("Frontend Tests") {
            steps {
                dir(env.FRONTEND_DIR) {
                    script {
                        sh """
                            npm install
                            npm test -- --passWithNoTests
                            npm run build
                        """
                    }
                }
            }
        }

        stage("Linting") {
            parallel {
                stage("Backend Linting") {
                    steps {
                        dir(env.BACKEND_DIR) {
                            sh """
                                pip install flake8
                                flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
                            """
                        }
                    }
                }
                stage("Frontend Linting") {
                    steps {
                        dir(env.FRONTEND_DIR) {
                            sh """
                                npm install eslint
                                npx eslint src/ --ext .js,.jsx --max-warnings 0
                            """
                        }
                    }
                }
            }
        }

        stage("Build Docker Images") {
            steps {
                dir(env.BACKEND_DIR) {
                    sh """
                        docker build -t portfolio-backend:${BUILD_NUMBER} .
                        docker tag portfolio-backend:${BUILD_NUMBER} portfolio-backend:latest
                    """
                }
                dir(env.FRONTEND_DIR) {
                    sh """
                        docker build -t portfolio-frontend:${BUILD_NUMBER} .
                        docker tag portfolio-frontend:${BUILD_NUMBER} portfolio-frontend:latest
                    """
                }
            }
        }

        stage("Push to Registry") {
            when {
                branch "main"
            }
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: "docker-registry-credentials", usernameVariable: "USERNAME", passwordVariable: "PASSWORD")]) {
                        sh """
                            echo $PASSWORD | docker login $DOCKER_REGISTRY -u $USERNAME --password-stdin
                            docker tag portfolio-backend:${BUILD_NUMBER} $DOCKER_REGISTRY/portfolio-backend:${BUILD_NUMBER}
                            docker tag portfolio-frontend:${BUILD_NUMBER} $DOCKER_REGISTRY/portfolio-frontend:${BUILD_NUMBER}
                            docker push $DOCKER_REGISTRY/portfolio-backend:${BUILD_NUMBER}
                            docker push $DOCKER_REGISTRY/portfolio-frontend:${BUILD_NUMBER}
                        """
                    }
                }
            }
        }

        stage("Deploy to Staging") {
            when {
                branch "main"
            }
            steps {
                sh """
                    echo "Deploying to staging environment..."
                    # Add staging deployment commands here
                """
            }
        }

        stage("Deploy to Production") {
            when {
                branch "main"
            }
            input {
                message "Deploy to production?"
                ok "Deploy"
            }
            steps {
                sh """
                    echo "Deploying to production environment..."
                    # Add production deployment commands here
                """
            }
        }
    }

    post {
        always {
            sh """
                docker system prune -f
            """
        }
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}
