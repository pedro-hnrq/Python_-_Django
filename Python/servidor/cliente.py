import socket


HOST ='localhost'
PORT = 8002

arquivo = open("Cesta.png", 'rb')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))

sock.send(input('Digite nome do arquivo').encode())
sock.send(arquivo.read())

confirmacao = sock.recv(1024)
if confirmacao == b'ok':
    print('mensagem recebida')