pipeline{
    agent any
    
    stages{
        stage('Checkout'){
            steps{
                git branch: 'main',
                url: 'https://github.com/Ghita-Takouit/Jenkins-Automated-CI-Pipeline.git',
                credentialsId: 'd09be296-d9a7-4e81-9530-2b31eb121b33'
            }
        }
        stage('Build'){
            steps{
                sh 'npm install'
            }
        }
        stage('Test'){
            steps{
                sh 'npm test'
            }
        }
        stage('Package'){
            steps{
                sh 'docker build -t jenkins-automated-ci-pipeline .'
            }
        }
        stage('Deploy'){
            steps{
                sh 'docker run -d -p 8080:8080 jenkins-automated-ci-pipeline'
            }
        }
    }
    post {
        success {
            mail to: 'rtakouit7@gmail.com',
                 subject: "Build Successful: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "The build was successful. You can check the details at ${env.BUILD_URL}"
        }
        failure {
            mail to: 'rtakouit7@gmail.com',
                 subject: "Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "The build failed. Please check the logs: ${env.BUILD_URL}"
        }
    }
}