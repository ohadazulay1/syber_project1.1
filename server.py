import socket
import os
from _thread import *
import sqlite3

from sereverHelper import ServerHelper

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0
DB_connection = sqlite3.connect('database.db', check_same_thread=False)
DB_cursor = DB_connection.cursor()
LOGIN_NUM = 0
SIGN_UP = 1
STARTING_SCORE = "0"
dataBaseHelper = ServerHelper()

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(5)
def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        decoded_data = data.decode()
        print("decoded data: " + decoded_data)
        guideNum = decoded_data[0]
        print("guidenum " + guideNum)
        newData = decoded_data[1:]
        print("newdata: " + newData)
        if guideNum == '0':
            if dataBaseHelper.login(newData, DB_cursor, DB_connection):
                message = '0there is a user with this username and password'
                print('there is a user with this username and password')
            else:
                message = '1there is no user with this username and password'
                print('there is not a user with this username and password')

        elif guideNum == "1":
            if dataBaseHelper.signUp(newData, DB_cursor, DB_connection, STARTING_SCORE):
                message = '0You are now in the DB'
                print('You are now in the DB')
            else:
                message = '1A user with the same username is already exist in the system'
                print('A user with the same username is already exist in the system')
                #צריך להחזיר תשובה לשרת כדי שהמשתמש יוכל להחליף שם משתמש או לעשות LOGIN
        response = message
        print(response)
        connection.sendall(str.encode(response))
        print("from client: " + data.decode())
        if not data:
            break
    connection.close()
while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()