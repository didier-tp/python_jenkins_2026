pipeline {
    //agent any
    agent {
        docker {
            //image "python:3.13"
	    image "python_venv_pytest"
            //avec python_venv_pytest image python améliorée comportant pytest en plus
        }
    }
environment{
	dockerhub_credential_id='credential_dockerhub_didierdefrance69'
	docker_registry= 'https://registry.hub.docker.com'
	docker_image_name='didierdefrance69/python_mensualite_api:1'
}
    stages {
        //stage('from_git') {
        //    steps {
        //        git url : 'https://github.com/didier-tp/python_jenkins_2026' , branch : 'main'
        //        }
        //}
        stage('ls python') {
            steps {
                echo 'Hello World !'
                sh 'python3 --version'
                sh 'ls *.py'
            }
		}
	stage('tests unitaires python') {
            steps {	
			     sh 'pytest -s test_mensualite.py'
			}
        }
	stage('build_docker_image') {
		steps {
script{
dockerImage = docker.build(docker_image_name)
}
}
}
stage('push_docker_image') {
steps {
script{
docker.withRegistry( docker_registry, dockerhub_credential_id ) {
dockerImage.push()
}
}
}
}
    }
}
