pipeline {
    agent any
    triggers {
       githubPush()
    }
    stages {
        stage('Stage 1') {
            steps {
                echo 'Initial stage' 
            }
        }
    }
}