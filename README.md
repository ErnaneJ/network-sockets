# Projeto de Programação com Sockets

Este repositório contém as soluções para as tarefas práticas de programação com sockets da disciplina DCA3605 - Redes de Computadores, ministrada pelo professor Carlos Manuel Dias Viegas na Universidade Federal do Rio Grande do Norte.

## Estrutura do Projeto

- **references/**: Contém os arquivos de código fornecidos pelo professor como referência para a implementação.
- **src/TaskA/**: Código fonte para a **Tarefa A - Sistema de Transferência de Arquivos**.
- **src/TaskB/**: Código fonte para a **Tarefa B - Sistema de Mensagens (Bate-Papo)**.

## Tarefa A: Sistema de Transferência de Arquivos

O sistema permite o upload e download de arquivos entre cliente e servidor utilizando sockets TCP.

### Como executar (TaskA)

1. Navegue até o diretório `src/TaskA`.
2. Execute o servidor:

    ```bash
    python server.py
    ```

3. Em outra janela/terminal, execute o cliente

   ```bash
   python client.py
   ```

4. Utilize os comandos a seguir no cliente
   - **Upload**: `upload nome_do_arquivo`
   - **Download**: `download nome_do_arquivo`

Os diretórios `client_files` e `server_files` simulam o sistema de armazenamento do cliente e do servidor. Ao realizar o experimento de troca de arquivos é possível observar a transferência de arquivos entre as pastas mencionadas.

## Tarefa B: Sistema de Mensagens (Bate-Papo)

Uma aplicação de chat utilizando sockets UDP. O cliente envia mensagens ao servidor, que responde. Suporta múltiplos clientes simultaneamente.

### Como executar (TaskB)

1. Navegue até o diretório `src/TaskB`.
2. Execute o servidor

   ```bash
   python server.py
   ```

3. Em outra janela/terminal, execute o cliente:

   ```bash
   python client.py
   ```

4. Digite mensagens no cliente para enviar ao servidor. O servidor pode responder diretamente.
5. O servidor consegue lidar com múltiplos usuários e responder individualmente cada um deles.

## Tecnologias

- Linguagem: Python 3
- Bibliotecas padrão: `socket`, `os`

## Autores

- **Ernane Ferreira Rocha Junior (@ERnaneJ)**
- **Quelita Miriam Nunes Ferraz (@Quelita2)**
