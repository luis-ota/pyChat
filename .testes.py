import tkinter as tk
from tkinter import Canvas, Label, Entry, Button
import threading
import socket
import time

class ExemploJanela:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.root.title("Exemplo Janela")

        self.indicador_conexao = Canvas(self.root, width=40, height=40, bg='white')
        self.indicador_conexao.place(relx=0.5, rely=0.85, anchor='center')
        self.indicador_conexao.create_oval(5, 5, 35, 35, outline='black', width=2)

        self.label_tentando_conectar = Label(self.root, text='Tentando conectar...', font=("Sans-serif", 12))
        self.label_tentando_conectar.place(relx=0, rely=0.9, relwidth=1, relheight=.1)

        self.conectar_button = Button(self.root, text='Conectar', command=self.client, font=("Sans-serif", 12))
        self.conectar_button.place(relx=.25, rely=.7, relwidth=.5, relheight=.2)

    def atualizar_indicador(self):
        angle = 0
        while self.tentando_conectar:
            self.indicador_conexao.delete('all')
            x0, y0, x1, y1 = 5, 5, 35, 35
            self.indicador_conexao.create_arc(x0, y0, x1, y1, start=angle, extent=45, style='arc', outline='black', width=2)
            angle += 15
            angle = angle % 360
            self.indicador_conexao.update()
            time.sleep(0.1)

    def client(self):
        try:
            self.tentando_conectar = True

            t = threading.Thread(target=self.atualizar_indicador)
            t.start()

            HOST = "localhost"  # Substitua pelo seu IP
            PORT = 9999
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))

            self.tentando_conectar = False
            t.join()  # Esperar pela conclusão da thread de atualização do indicador

            # Substitua essa parte pelo seu código de sucesso de conexão
            self.label_tentando_conectar.config(text='Conectado com sucesso!')

        except:
            self.tentando_conectar = False
            self.indicador_conexao.delete('all')  # Limpar o indicador
            self.label_tentando_conectar.config(text='*IP inválido, tente novamente')

    def iniciar(self):
        self.root.mainloop()

# Crie uma instância da classe e inicie a janela
exemplo_janela = ExemploJanela()
exemplo_janela.iniciar()
