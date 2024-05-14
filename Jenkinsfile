pipeline {
    agent any
    
    triggers {
       githubPush()
    }

    environment {
        env = 'prod'
        MONGODB_PWD = credentials('MONGODB_PWD')
        AWS_DEFAULT_REGION = 'eu-central-1'
    }

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Type check') {
            steps {
                sh 'cd .. ; ~/.local/bin/mypy prod-diskover-server --ignore-missing-imports --config-file ./prod-diskover-server/mypy.ini ; cd ./prod-diskover-server'
            }
        }

        stage('Execute') {
            steps {
                withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'AWS_KEYS', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                    sh 'echo Deployment Successfull'
                }
            }
        }
    }
}