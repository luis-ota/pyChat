# pyChat - Chat com Interface usando Socket

In [English](README.md) | Em [Português](README_PTBR.md)

##

Este é um projeto de chat cliente-servidor com interface gráfica, permitindo a comunicação entre vários computadores usando sockets em Python.

## Visão Geral

Este projeto consiste em duas partes principais: o servidor e o cliente. O servidor gerencia conexões entre clientes e encaminha mensagens, enquanto o cliente fornece uma interface gráfica para os usuários participarem do chat.

## Funcionalidades

- **Servidor:**
  - Gerencia conexões de clientes.
  - Encaminha mensagens entre clientes.
  - Permite comunicação privada entre usuários.

- **Cliente:**
  - Interface gráfica amigável.
  - Envio de mensagens para todos os participantes.
  - Envio de mensagens privadas para usuários específicos.

## Requisitos

- **Servidor e Cliente:**
  - Python 3.x

- **Cliente:**
  - Biblioteca `customtkinter` (instalável via `pip install customtkinter`)

## Como Usar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/luis-ota/pyChat.git

   ```

2. **Configuração do Servidor:**
   - No  `servidor.py`, especifique o IP da máquina que será o servidor.
   - Desative o firewall do servidor para permitir conexões.

3. **Configuração do Cliente:**
   - Coloque o IP do servidor no código do cliente.

4. **Inicie o Servidor:**
   - Execute o script `servidor.py`.

5. **Inicie os Clientes:**
   - Execute o script `app/main.py` em cada máquina que deseja participar do chat.

Agora, com o servidor e os clientes em execução, os usuários podem se comunicar entre si através do chat. Certifique-se de que todas as máquinas estejam na mesma rede para garantir a comunicação adequada.
  
