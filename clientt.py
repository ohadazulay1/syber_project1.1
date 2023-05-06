import socket
import login
from firstWin22 import Ui_firstWindow

class Client:
    def __init__(self):
        self.ClientMultiSocket = socket.socket()
        self.host = '127.0.0.1'
        self.port = 2004
        print('Waiting for connection response')
        try:
            self.ClientMultiSocket.connect((self.host, self.port))
        except socket.error as e:
            print(str(e))
        res = self.ClientMultiSocket.recv(1024)
        print(res.decode('utf-8'))
        #gui.first()
        #login.start()
#        res = ClientMultiSocket.recv(1024)
 #       login = Ui_firstWindow()
  #      userPass = login.signInPressed()
   #     Input = input('Hey there: ')
    #    self.ClientMultiSocket.send(str.encode(Input))
     #   res = self.ClientMultiSocket.recv(1024)
      #  print(res.decode('utf-8'))


    def login(self, username, password):
        message = "0"+username+","+password
        self.ClientMultiSocket.send(str.encode(message))
        res = self.ClientMultiSocket.recv(1024)
        data = res.decode('utf-8')
        guideNum = data[0]
        newData = data[1:]
        print(newData)
        if guideNum == "0":
            print("true")
            return True
        elif guideNum == "1":
            print("false")
            return False



    def signUp(self, username, password):
        message = "1"+username+","+password
        self.ClientMultiSocket.send(str.encode(message))
        res = self.ClientMultiSocket.recv(1024)
        data = res.decode('utf-8')
        print(data)
        guideNum = data[0]
        print(guideNum)
        newData = data[1:]
        print(newData)
        if guideNum == "0":
            print("true")
            return True
        elif guideNum == "1":
            print("false")
            return False

#if __name__ == "__main__":
  #  c = Client()
    #c.login("yaniv", "yyaanniivv")
 #   c.signUp("yaniv", "yyaanniivv")

