pipeline{
    agent any

    stages {
        stage("Install Dependencies"){
            steps{
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pip install bandit pip-audit
                '''
            }
        }

        stage("Run Tests"){
            steps{
                sh '''
                    . venv/bin/activate
                    pytest
                '''
            }
        }

        stage("SAST - Bandit"){
            steps{
                sh'''
                    . venv/bin/activate
                    bandit -r . -x ./venv,./test_app.py
                '''
            }
        }

        stage("Dependency Scan - pip-audit"){
            steps{
                sh'''
                    . venv/bin/activate
                    pip-audit -r requirements.txt
                '''
            }
        }
    }
}