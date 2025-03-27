pipeline {
    agent any

    stages {
        stage("Checkout") {
           steps {
                script {
                    def gitCheckout = checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'github', url: 'https://github.com/Gideon-Tee/flask-jenkins-pipeline-test.git']]])
                }
           }
        }

        stage("Setup environment") {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
    }
}

