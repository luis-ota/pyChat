from customtkinter import *
import socket
import threading as th
from datetime import datetime




def ChatApp():
    global sock, dados

    janela = CTk()

    class App():
        def __init__(self):
            self.janela = janela
            self.tela()
            self.frameLateral()
            self.frameMain()
            self.InputUsuario()
            self.jaExibindo = []
            self.usuariosConectados = []
            self.usuario = []
            janela.mainloop()

        def tela(self):
            self.janela.title('chat')
            self.janela.configure(background='#212225')
            self.janela.geometry('900x600')
            self.janela.resizable(True, True)
            self.janela.minsize(width=800, height=500)
            self.top = .03
            self.heigh = .94
            self.numBalao = 0
            self.font = ("Sans-serif", 21)

        def exibirChat(self, subir):
            if self.chatUnderAtual == subir:
                pass
            else:
                subir.lift(self.chatUnderAtual)
                self.ultimoChat = self.chatUnderAtual
                self.chatUnderAtual = subir

        def frameLateral(self):
            self.botoesChatLateral=[]
            self.chats_lateral = CTkScrollableFrame(self.janela)
            self.chats_lateral.place(relx=.02,
                                     rely=self.top,
                                     relwidth=.2,
                                     relheight=self.heigh)

            self.chatGeral = CTkButton(self.chats_lateral,
                                       text='geral',
                                       font=self.font, height=50,
                                       command=lambda: self.exibirChat(self.chatGeralUnderFrame))
            self.chatGeral.pack(fill='both', expand=True, pady=2)
            self.chats = th.Thread(target=self.recebendo)
            self.chats.start()


        def recebendo(self):
            while True:
                dados = sock.recv(1024).decode()
                if dados:
                    try:
                        """if dados.split('§')[1] == 'usrList':
                            deletar = True if len(eval(dados.split('£')[1])) < len(self.usuariosConectados) else False

                            self.usuariosConectados = eval(dados.split('£')[1])
                            self.usuariosConectados.remove(self.usuario[0])

                            if self.usuariosConectados:
                                if not deletar:
                                    for user in self.usuariosConectados:
                                        if user not in self.botoesChatLateral:
                                            self.updateChatsLateral(usr=user)
                                            self.botoesChatLateral.append(user)
                                else:
                                    quaisDeletar = [x for x in self.usuariosConectados if x not in dados.split('£')[1]]
                                    for user in quaisDeletar:
                                        self.updateChatsLateral(usr=user, deletar=deletar)
                                        self.botoesChatLateral.remove(user)
                                        print('deletou botao')"""
                        int('a')
                    except:
                        self.mensagemRecebida = dados
                        if self.mensagemRecebida:
                            self.usuariosConectados.append(self.mensagemRecebida.split('¢')[1])
                            self.balaoMensagem(fromUsr=self.mensagemRecebida.split('¢')[1])

        def updateChatsLateral(self, usr='', deletar=False):
            try:
                if not deletar:
                    #exec(f"self.chat{usr}UnderFrame = CTkFrame(self.frameMensagens, fg_color='transparent')")
                    #exec(f"self.chat{usr}UnderFrame.place(relx=0, rely=0, relwidth=1, relheight=self.heigh + .05)")
                    #exec(f"self.chat{usr}UpFrame = CTkScrollableFrame(self.chat{usr}UnderFrame)")
                    #exec(f"self.chat{usr}UpFrame.place(relx=0, rely=0, relwidth=1, relheight=1)")
                    exec(f"self.chat{usr} = CTkButton(self.chats_lateral, text='{usr} esntrou', font=self.font, height=50, command=lambda: print('{self.botoesChatLateral}'))")
                    exec(f"self.chat{usr}.pack(fill='both', expand=True, pady=2)")
                    self.ultimoChat = self.chatUnderAtual
                    exec(f"self.chatUnderAtual = self.chat{usr}UnderFrame")
                    self.exibirChat(self.ultimoChat)

                else:
                    exec(("self.chat{usr}UnderFrame.destroy()"))
            except:
                print(usr)

        def frameMain(self):
            self.mainChat = CTkFrame(self.janela)

            self.mainChat.place(relx=.24,
                                rely=self.top,
                                relwidth=.74,
                                relheight=self.heigh)

            self.frameMensagens = CTkFrame(self.mainChat)
            self.frameMensagens.place(relx=.02,
                                      rely=.02,
                                      relwidth=.96,
                                      relheight=.85)


            self.chatGeralUnderFrame = CTkFrame(self.frameMensagens, fg_color="transparent")
            self.chatGeralUnderFrame.place(relx=0, rely=0, relwidth=1, relheight=self.heigh + .05)
            self.chatGeralUpFrame = CTkScrollableFrame(self.chatGeralUnderFrame)
            self.chatGeralUpFrame.place(relx=0,
                                        rely=0,
                                        relwidth=1,
                                        relheight=1
                                        )
            self.chatUnderAtual = self.chatGeralUnderFrame
            self.chatUpAtual = self.chatGeralUpFrame

            self.digMensagem = CTkFrame(self.mainChat)
            self.digMensagem.place(relx=.02,
                                   rely=.88,
                                   relwidth=.96,
                                   relheight=.1)

            self.inputMensagem = CTkEntry(self.digMensagem, font=self.font)

            self.inputMensagem.bind("<Return>", self.balaoMensagem)

            self.inputMensagem.place(relx=0,
                                     rely=0,
                                     relwidth=.91,
                                     relheight=1)

            self.enviarBtn = CTkButton(self.digMensagem, text='>', command=self.balaoMensagem, font=('Sans-serif', 30))
            self.enviarBtn.place(relx=.92,
                                 rely=.1,
                                 relwidth=.07,
                                 relheight=.8)

        def balaoMensagem(self, fromUsr=None, toUsr=False, entrando=False):
            hora = datetime.now().strftime('%H:%M')

            if entrando:
                mensagem = f'{self.usuario[0]} entrou do chat'
                if mensagem == '/q' or mensagem == '/Q':
                    mensagem = f'{self.usuario[0]} saiu do chat'
                if self.chatUnderAtual == self.chatGeralUnderFrame and len(mensagem) > 0:

                    user_label = CTkLabel(self.chatGeralUpFrame, text=f'{self.usuario[0]} - {hora}',
                                          font=("Sans-serif", 14))
                    user_label.pack(side="top", anchor="ne")

                    boxMensagem = CTkTextbox(self.chatGeralUpFrame, width=300, height=50, font=self.font)
                    boxMensagem.pack(expand=True, anchor="e", pady=6)

                    boxMensagem.configure(state='normal')
                    boxMensagem.insert('end', mensagem)
                    boxMensagem.configure(state='disabled')
                    self.inputMensagem.delete(0, 'end')
                    self.numBalao += 1
            else:
                if fromUsr in self.usuariosConectados:
                    mensagem = self.mensagemRecebida.split('£')[1]
                    if 'geral' == self.mensagemRecebida.split('$')[1].split(' ')[-1]:
                        user_label = CTkLabel(self.chatGeralUpFrame, text=f'{fromUsr} - {hora}', font=("Sans-serif", 14))
                        user_label.pack(side="top", anchor="w")

                        boxMensagem = CTkTextbox(self.chatGeralUpFrame, width=300, height=50, font=self.font,
                                                 fg_color='#1f6aa5')
                        boxMensagem.pack(expand=True, anchor="w", pady=6)

                        boxMensagem.configure(state='normal')
                        boxMensagem.insert('end', mensagem)
                        boxMensagem.configure(state='disabled')
                        self.inputMensagem.delete(0, 'end')
                        self.numBalao += 1
                    else:
                        print(mensagem)
                else:
                    mensagem = self.inputMensagem.get()
                    if mensagem == '/q' or mensagem == '/Q':
                        mensagem = f'{self.usuario[0]} saiu do chat'
                        desligar = True
                    else:
                        desligar = False
                    if self.chatUnderAtual == self.chatGeralUnderFrame and len(mensagem) > 0:
                        sock.sendall(str.encode(f'§geral§: £{mensagem}£'))

                        user_label = CTkLabel(self.chatGeralUpFrame, text=f'{self.usuario[0]} - {hora}', font=("Sans-serif", 14))
                        user_label.pack(side="top", anchor="ne")

                        boxMensagem = CTkTextbox(self.chatGeralUpFrame, width=300, height=50, font=self.font)
                        boxMensagem.pack(expand=True, anchor="e", pady=6)

                        boxMensagem.configure(state='normal')
                        boxMensagem.insert('end', mensagem)
                        boxMensagem.configure(state='disabled')
                        self.inputMensagem.delete(0, 'end')
                        self.numBalao += 1

                    if desligar:
                        self.janela.destroy()
                        exit(0)

        def InputUsuario(self):
            recebendo = th.Thread(target=self.recebendo)
            recebendo.start()

            def Entrar(a=None):
                invalido = False
                primeira = True
                for letra in nomeUsuario.get():
                    if primeira:
                        if letra is int:
                            invalido = True
                        primeira = False
                    if letra not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890':
                        invalido = True

                if nomeUsuario.get() and not invalido and nomeUsuario.get() not in self.usuariosConectados and len(nomeUsuario.get())<10:
                    self.usuario.append(nomeUsuario.get())
                    bemvindo = CTkLabel(self.chatGeralUpFrame, text=f'bem vindo, {nomeUsuario.get()}', font=self.font)
                    bemvindo.pack(expand=True, anchor="s", pady=5)
                    self.janela.title(f'chat: {self.usuario[0]}')
                    sock.sendall(str.encode(f'usuario: §{nomeUsuario.get()}§'))
                    self.balaoMensagem(entrando=True)
                    input.destroy()
                else:
                    try:
                        self.nomeInvalido.destroy()
                    except:
                        pass
                    self.nomeInvalido = CTkLabel(centro, text='*Nome invalido ou já utilizado', font=("Sans-serif", 16),
                                                 text_color='red', fg_color='transparent', anchor="w")
                    self.nomeInvalido.place(relx=0,
                                            rely=.57,
                                            relwidth=1,
                                            relheight=.1)

            input = CTkFrame(self.janela)

            input.place(relx=0,
                        rely=0,
                        relwidth=1,
                        relheight=1)

            centro = CTkFrame(input, fg_color="transparent")
            centro.place(relx=.24,
                         rely=.3,
                         relwidth=.52,
                         relheight=.37)

            label = CTkLabel(centro, text='Digite o nome do seu usuario', font=self.font)

            label.place(relx=0,
                        rely=.2,
                        relwidth=1,
                        relheight=.1)

            nomeUsuario = CTkEntry(centro, font=self.font)

            nomeUsuario.bind("<Return>", Entrar)

            nomeUsuario.place(relx=0,
                              rely=.37,
                              relwidth=1,
                              relheight=.2)

            self.entrar = CTkButton(centro, text='Entrar', command=Entrar, font=self.font)
            self.entrar.place(relx=.25,
                              rely=.7,
                              relwidth=.5,
                              relheight=.2)

    App()



def Client():
    global sock
    HOST = "127.0.0.1" # str(input('digite o ip do servidor: '))
    PORT = 9999

    # quero me conectar em 127.0.0.1:9999
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # como a conexão é tcp precisamos de um conect
    sock.connect((HOST, PORT))  # acende o accep do servidor


if __name__ == '__main__':
    Client()
    ChatApp()
