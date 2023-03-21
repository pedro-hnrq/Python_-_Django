import socket

HOST ='localhost'
PORT = 8002

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((HOST, PORT))

sock.listen(5)

while True:
    novoSock, _ = sock.accept()
    nomeArquivo = novoSock.recv(1024).decode()
    novoArquivo = novoSock.recv(1000000000)
     
    with open(f'arquivos/{nomeArquivo}.png','wb') as arq:
        arq.write(novoArquivo)

    novoSock.send(b'ok')