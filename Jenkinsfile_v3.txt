pipeline {
    //agent any
    agent {
        docker {
            //image "python:3.13"
	    image "python_venv_pytest"
            //avec python_venv_pytest image python améliorée comportant pytest en plus
        }
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
    }
}