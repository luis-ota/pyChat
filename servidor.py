import socket as s
import threading as th

conexoes = {}
usuarios = []


def obter_ip_local():
    try:
        # Obtém o nome do host
        host_name = s.gethostname()

        # Obtém o endereço IP associado ao nome do host
        ip_address = s.gethostbyname(host_name)
        return ip_address
    except Exception as e:
        print(f"Erro ao obter o endereço IP: {str(e)}")


def server():
    global sock, conn, ender, conexoes, usuarios
    HOST = obter_ip_local()  # str(input('digite o ip da maquina que sera o servidor: '))  # 127.0.0.1
    PORT = 9999

    # inicializar o socket com os seus parametros basicos (IPV4 e TCP)
    # AF_INET IPV4
    # SOCK_STREAM É TCp

    sock = s.socket(s.AF_INET, s.SOCK_STREAM)

    # Vincular o socket do servidor: endereço ip : porta --> bind

    # localhost:9999
    sock.bind((HOST, PORT))

    # servidor começa a escutar conexões
    sock.listen()  # abre a porta

    print(f'o servidor {HOST}:{PORT} esta aguardando conexão')

    # aceitamos a conexão
    # conn é o socket do cliente
    # ender é o endereço da porta
    while True:
        conn, ender = sock.accept()
        while conn:
            try:
                dados = conn.recv(1024).decode()
            except:
                break

            if dados:
                usuario = dados.split('§')[1::2][0]
                if usuario:
                    conexoes[usuario] = conn
                    usuarios.append(usuario)
                    exec(f'{usuario} = th.Thread(target=conexao, args=("{usuario}",), name="{usuario}")')
                    exec(f'{usuario}.start()')
                del conn
                sock.listen()
                break


def conexao(usuario):
    global conexoes, sock, conn, ender, usuarios
    print(f'servidor: Conectado em: {ender} para o usuario: {usuario}')
    broadcast(usuario, f'{usuario} entrou no chat', False)
    while True:
        try:
            dados = conexoes[usuario].recv(1024).decode()  # bytes de dados
        except:
            print(f'servidor: finalizando thread do usuario {usuario}')
            try:
                conexoes.pop(usuario)
            except:
                pass
            break
        toUser = dados.split('§')[1]
        mensagem = dados.split('£')[1]
        try:
            saindo = dados.split('*')[1]
        except:
            saindo = False

        if toUser in conexoes:
            conexoes[toUser].sendall(str.encode(f'${usuario}$: £{mensagem}£'))
            print(toUser)
        elif toUser == 'geral':
            broadcast(usuario, mensagem, saindo)


def broadcast(usr, msg, saindo):
    global conexoes, sock, conn, ender, usuarios
    if not saindo:
        for usuario in conexoes:
            if usr != usuario:
                conexoes[usuario].sendall(str.encode(f'$¢{usr}¢ no geral$: £{msg}£'))
        print(f'{usr} no geral: {msg}')
    else:
        try:
            conexoes.pop(usr)
        except:
            pass
        for usuario in conexoes:
            if usr != usuario:
                conexoes[usuario].sendall(str.encode(f'$¢{usr}¢ no geral$: £{msg}£'))
        print(f'{usr} no geral: {msg}')


if __name__ == '__main__':
    server()
