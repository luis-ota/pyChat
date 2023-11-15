# pyChat - Chat com Interface usando Socket

Este é um projeto de chat cliente-servidor com interface gráfica, permitindo a comunicação entre vários computadores usando sockets em Python.

## Conteúdo

1. [Visão Geral](#visão-geral)
2. [Funcionalidades](#funcionalidades)
3. [Requisitos](#requisitos)
4. [Configuração](#configuração)
5. [Execução](#execução)
6. [Contribuições](#contribuições)
7. [Licença](#licença)

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

## Configuração

1. Clone o repositório:

   ```bash
   git clone https://github.com/luis-ota/pyChat.git
