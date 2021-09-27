pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                echo 'nothing to do'
            }
        }
        stage('test') {
            steps {
                sh 'python3 cylinderTest.py'
                sh 'python3 GeometryCalcWebTest.py'
            }
        }
    }
}
