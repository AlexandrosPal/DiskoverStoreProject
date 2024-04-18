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
        stage('Setup') {
            steps {
                sh 'cd ~/home/ec2-user/DiskoverProject && git pull'
            }
        }

        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Execute') {
            steps {
                withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'AWS_KEYS', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                    sh 'python EC2Scripts/Executions/analysis_execution.py'
                }
            }
        }
    }
}