import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hook():
    
    prev_id = subprocess.check_output(['sudo', 'docker', 'ps'],  universal_newlines=True).split('\n')[1].split('        ')[0]
    
    subprocess.call(['sudo', 'docker', 'stop', prev_id])
    subprocess.call(['sudo', 'docker', 'rm', prev_id]) 
    subprocess.call(['sudo', 'docker', 'build', '--no-cache', '-t',  'hannam', '/home/ubuntu/HB-docker'])
    subprocess.call(['sudo', 'docker', 'run', '-d', '-p', '8888:3000', 'hannam'])

    print('hook!!')
    return "hook response \n"
