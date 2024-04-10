pipeline {
    agent any
    triggers {
       githubPush()
    }
    stages {
        stage('Execute') {
            steps {
                sh 'pwd'
                dir('/home/ec2-user/DiskoverProject/EC2Scripts/Executions') {
                    sh 'pwd'
                    sh 'python analysis_execution.py'
        } 
            }
        }
    }
}