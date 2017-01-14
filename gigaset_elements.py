import re
from subprocess import Popen, PIPE, call

class GigasetElements:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def alarm_status(self):
        cmd = ['/home/pi/projects/keypad/gigaset_elements_status.sh', self.username, self.password]
        p = Popen(cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()

        status = stdout.strip()

        if status == 'HOME':
            return 'home'
        elif status == 'AWAY':
            return 'away'
        else:
            return 'unknown'
        
    def activate_alarm(self):
    	call(['gigasetelements-cli', '-u', self.username, '-p', self.password, '-m', 'away'])
    
    def deactivate_alarm(self):
    	call(['gigasetelements-cli', '-u', self.username, '-p', self.password, '-m', 'home'])
