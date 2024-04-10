pipeline {
    agent any
    triggers {
       githubPush()
    }
    stages {
        stage('Checkout') {
            steps {
                sh 'git pull && python ./EC2Scripts/Utils/switch_env.py'
            }
        }
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