pipeline {
    agent any
    triggers {
       githubPush()
    }
    stages {
        stage('Execute') {
            steps {
                sh 'python EC2Scripts/Executions/analysis_execution.py'
            }
        }
    }
}