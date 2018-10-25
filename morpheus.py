#!/usr/bin/env python3
import os
import socket
import sys
import argparse

from multiprocessing import Process
from sys import exit, platform
from protocols.ftp import BruteFTB
from protocols.ssh import BruteSSH

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

def error(msg):
    print(msg)
    sys.exit(1)

def verifySystem():
    if (platform.startswith('win32')):
        error("I'm sorry, use linux or mac osx")

def isAlive(host, protocol):
    service_port = socket.getservbyname(protocol)
    alive = socket.socket()
    alive.settimeout(1)
    status = alive.connect_ex((host, service_port))

    return status

def main():

    help_message = '''
    Arguments:
        --host,     -h      target
        --user,     -u      user, default is root
        --wordlist, -w      wordlist used for the attack
        --protocol, -p      protocol
    
    Protocol supported:
        ftp
        ssh

    Example:
        python mporheus.py -h 192.168.1.1 -u root -w wordlist.txt -p ftp
    '''
    
    parser = argparse.ArgumentParser(add_help=False, usage=help_message)
    parser.add_argument('--host', '-h',     action="store", dest="host",\
                            required=True)
    
    parser.add_argument('--protocol', '-p',  action="store", dest="protocol",\
                            required=True)
   
    parser.add_argument("--user", '-u',     action="store", dest="user",\
                            default="root", required=False)
   
    parser.add_argument("--wordlist", '-w', action="store", dest="wordlist",\
                            required=True)

    given_args = parser.parse_args()

    host        = given_args.host
    user        = given_args.user
    wordlist    = given_args.wordlist
    protocol    = given_args.protocol

    if (isAlive(host, protocol)) != 0:
        error("Host not responding on protocol {0}".format(protocol))

    if protocol == 'ftp':
        FTP = BruteFTB(host, user, wordlist)
        FTP.Checkout()
    
    elif protocol == 'ssh':
        SSH = BruteSSH(host, user, wordlist)
        SSH.Checkout()

if __name__=='__main__':
    banner()
    verifySystem()
    main()
