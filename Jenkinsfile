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
                sh 'python3 ./geometry_calculator_web/cylinderTest.py'
            }
        }
    }
}
