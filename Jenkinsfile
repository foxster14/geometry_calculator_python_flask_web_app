node {
  def remote = [:]
  remote.name = 'flaskserver'
  remote.host = '192.168.56.104'
  remote.user = 'joeaxberg'
  remote.password = 'axbRTR95'
  remote.allowAnyHosts = true
  stage('Verify SSH') {
    sshCommand remote: remote, command: "ls -lrt"
    sshCommand remote: remote, command: "for i in {1..5}; do echo -n \"Loop \$i \"; date ; sleep 1; done"
  }
}
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
        stage('deploy'){
            steps {
                sshPut remote: remote, from: 'geometry_calculator_web.zip', into: '.'
            }
        }
    }
}
