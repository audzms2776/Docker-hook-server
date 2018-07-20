import subprocess

subprocess.call(['export', 'FLASK_APP=app.py'])
subprocess.call(['nohup', 'flask', 'run', '--host=0.0.0.0', '--port=3333'])