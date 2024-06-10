pipeline {
    agent any

    environment {
        EC2_IP = '54.226.60.27'
        SSH_CREDENTIALS_ID = 'ssh_key'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/rushikeshmj/Flask-web-application.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                pip install gunicorn
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
                # Add your test commands here
                '''
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(['SSH_CREDENTIALS_ID']) {
                    sh '''
                    scp -r * ec2-user@${EC2_IP}:/home/ec2-user/Flask-web-application/
                    ssh ec2-user@${EC2_IP} << EOF
                    cd /home/ec2-user/Flask-web-application
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                    pip install gunicorn
                    pkill -f gunicorn || true
                    nohup gunicorn --bind 0.0.0.0:8000 run:app &
                    EOF
                    '''
                }
            }
        }
    }
}
