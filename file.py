pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                sh 'python3 --version'
            }
        }
      stage('Hello') {
          steps {
                sh 'file1.py'
            }
        }
    }
}
