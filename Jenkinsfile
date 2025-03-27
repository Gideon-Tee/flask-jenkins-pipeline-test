pipeline {
    agent any

    parameters {
        string(name: 'BUILD_VERSION', defaultValue: 'latest', description: 'Enter the build verison for the image')
    }

    stages {
        stage("Checkout") {
           steps {
                script {
                    def gitCheckout = checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'github', url: 'https://github.com/Gideon-Tee/flask-jenkins-pipeline-test.git']]])
                }
           }
        }

        stage("Build") {
            steps {
                echo "Test the application before building"
                sh 'python3 -m pytest'
                sh 'docker build -t flask-hello-world:${BUILD_VERSION}'
            }
        }
    }
}

