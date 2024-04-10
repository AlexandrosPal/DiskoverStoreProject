pipeline {
    agent any
    triggers {
       githubPush()
    }
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Environment') {
            steps {
                sh 'python ./EC2Scripts/Utils/switch_env.py'
            }
        }
        stage('Execute') {
            steps {
                sh 'python EC2Scripts/Executions/analysis_execution.py'
            }
        }
    }
}