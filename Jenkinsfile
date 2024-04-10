pipeline {
    agent any
    
    triggers {
       githubPush()
    }

    environment {
        env = 'prod'
        MONGODB_PWD = credentials('MONGODB_PWD')
    }

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Execute') {
            steps {
                sh 'python EC2Scripts/Executions/analysis_execution.py'
            }
        }
    }
}