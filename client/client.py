import socket
import threading as th
import time


# informações do servidor

HOST = '127.0.0.1'
PORT = 9999

# quero me conectar em 127.0.0.1:9999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# como a conexão é tcp precisamos de um conect
sock.connect((HOST, PORT))  # acende o accep do servidor

usuario = input('digite seu user: ')
# agora o cliente envia dados
sock.sendall(str.encode(f'usuario: +{usuario}+'))


def recebendo():
    while True:
        dados = sock.recv(1024).decode()



def enviando():
    while True:
        sock.sendall(str.encode(f'{usuario}: {input("digite sua mensagem:")}'))


th.Thread(target=enviando).start()
th.Thread(target=recebendo).start()