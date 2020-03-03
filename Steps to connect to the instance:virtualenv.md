Steps to connect to the instance/virtualenv

Copy/paste
ssh -i "SoftwareEngineering.pem" ec2-user@ec2-18-222-133-130.us-east-2.compute.amazonaws.com

After sshing, run these two commands
virtualenv --python=python3 virtualenvs/myenv
source virtualenvs/myenv/bin/activate