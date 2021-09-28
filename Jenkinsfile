def remote = [name: 'flaskserver', host: '192.168.56.104', user: 'joeaxberg', password: 'axbRTR95', allowAnyHosts: true]
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
            }
        }
        stage('package'){
            steps {
                sh 'tar -cf geometry_calculator_web.tar *'
            }
        }
        stage('deploy'){
            steps {
                sshPut remote: remote, from: 'geometry_calculator_web.tar', into: '.'
            }
        }
    }
}
