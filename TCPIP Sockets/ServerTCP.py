from socket import *

serverName = "127.0.0.1"
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)

print("The server is ready to receive")

while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()

    try:
        with open(sentence, "r") as file:
            content = file.read(1024)
            connectionSocket.send(content.encode())
    except FileNotFoundError:
        connectionSocket.send("File not found".encode())

    connectionSocket.close()
