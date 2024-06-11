pipeline {
    agent any

    environment {
        EC2_IP = '3.83.234.183'
        SSH_CREDENTIALS_ID = 'ssh_key'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/rushikeshmj/Flask-web-application.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv ~/.venv
                source ~/.venv/bin/activate
                pip3 install -r requirements.txt
                pip3 install gunicorn
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
                    scp -r * ec2-user@${EC2_IP}:/home/ec2-user/sample-app/
                    ssh ec2-user@${EC2_IP} << EOF
                    cd /home/ec2-user/sample-app
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
