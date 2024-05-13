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
                sh 'cd .. ; mypy --package DiskoverProject --ignore-missing-imports ; cd ./DiskoverProject'
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