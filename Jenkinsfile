pipeline {
    agent any
    triggers {
       githubPush()
    }
    stages {
        stage('Execute') {
            steps {
                dir('/home/ec2-user/DiskoverProject/EC2Scripts/Executions') {
                    sh 'python analysis_execution.py'
        } 
            }
        }
    }
}