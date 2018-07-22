import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hook():
    
    # find docker id 
    prev_id = subprocess.check_output(['sudo', 'docker', 'ps'],  universal_newlines=True).split('\n')[1].split('        ')[0]
    
    # stop docker ps
    subprocess.call(['sudo', 'docker', 'stop', prev_id])
    subprocess.call(['sudo', 'docker', 'rm', prev_id]) 
    
    # rebuild docker image and start
    subprocess.call(['sudo', 'docker', 'build', '--no-cache', '-t',  'HbServer', '/home/ec2-user/HB-docker'])
    subprocess.call(['sudo', 'docker', 'run', '-d', '-p', '8888:3000', 'HbServer'])

    print('hook!!')
    return "hook response \n"
