import socket, os
import threading, sys

os.system("color a")


class Serverr:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        self.sock.bind(('0.0.0.0', 10000))
        self.sock.listen(1)

    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            for connection in self.connections:
                connection.send(data)
            if not data:
                print(str(a[0]) + ':' + str(a[1]), "Disconnected")
                break
    
    def run(self):
        print("                                             Anonym Chat                              ")
        print("               ---------------------------------------------------------------------- ")
        print("              {'             © All Rights Reserved by Simple Apps INC.              '}")
        print("               ---------------------------------------------------------------------- ")
        print("                {'            Visit us: https://www.simpleappsinc.com             '}")
        print("                 ------------------------------------------------------------------   ")
        print("                  {'                Maden by: Ata Yigit Ustundag                '}")
        print("                   --------------------------------------------------------------     ")
        print("")
        while True:
            c, a = self.sock.accept()
            cThread = threading.Thread(target = self.handler, args = (c,a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(str(a[0]) + ':' + str(a[1]), "Connected")
#words = list()
class Client:
    #n = "<illegal word>"
    #words = list()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def sendMsg(self):
        while True:
            self.sock.send(bytes(input(">>>> "), 'utf-8'))
            #gg = self.sock.send(bytes(input("You: "), 'utf-8'))
            #words.append(gg)
            #for n in words:
                #print("You said fuck")
                #words.remove(gg)
    def __init__(self, address):
        self.sock.connect((address, 10000))

        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print(str(data, 'utf-8'))
if(len(sys.argv) > 1):
    client = Client(sys.argv[1])
else:
    server = Serverr()
    os.system("start www.simpleappsinc.com")
    server.run()
print("------------------------")
