pipeline {
    agent { label 'master' }
    stages {
        stage('build') {
            steps {
                echo "Hello World!"
            }
        }
        
        stage('Test') {
            steps {
             echo "Testing application !"   
            }
        }
        
        stage('Deploy') {
            steps {
             echo "Deploying application !"   
            }
        }
    }
}
