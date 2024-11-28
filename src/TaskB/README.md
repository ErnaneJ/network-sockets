# Chat UDP - Sistema de Mensagens (Bate-papo)

## Descrição

Este projeto implementa um sistema de mensagens baseado em UDP, permitindo que vários clientes se conectem a um servidor e troquem mensagens em tempo real. A comunicação é feita de forma simples e eficiente, utilizando o protocolo UDP para a troca de mensagens entre o servidor e os clientes. O projeto foi desenvolvido como parte da disciplina de Redes de Computadores (DCA0113) da Universidade Federal do Rio Grande do Norte.

O sistema é composto por duas partes principais:

1. **Servidor (ChatServer)**: Responsável por receber mensagens do cliente e responder elas
2. **Cliente (ChatClient)**: Permite que o usuário envie e receba mensagens do servidor, utilizando um nome de usuário para identificar as mensagens enviadas.

## Funcionalidades

- **Chat entre cliente e servidor**: Vários clientes podem se conectar ao servidor para envio de mensagens.
- **Saída do chat**: O usuário e o servidor pode digitar `exit` para sair do chat e encerrar a conexão.

## Tecnologias Utilizadas

- **Python 3.x**
- **Sockets UDP**: Protocolo de comunicação sem conexão utilizado para a troca de mensagens.

## Estrutura do Projeto

O projeto é dividido em dois arquivos principais:

- **chat_server.py**: Implementação do servidor que gerencia a comunicação entre os clientes.
- **chat_client.py**: Implementação do cliente que envia e recebe mensagens do servidor.

## Como Executar o Projeto

### **0. Se necessário utilize o VENV**

```bash
pwd #=> $PATH/(...)/network-sockets/src/TaskB
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Passo 1: Iniciar o Servidor

Primeiro, inicie o servidor. Ele ficará aguardando as conexões dos clientes.

1. Abra um terminal.
2. Navegue até o diretório onde o arquivo `chat_server.py` está localizado.
3. Execute o servidor com o seguinte comando:

   ```bash
   python chat_server.py
   ```

   O servidor irá iniciar e ficará ouvindo na porta `5002` esperando pelas mensagens dos clientes.

### Passo 2: Iniciar os Clientes

Agora, inicie os clientes. Cada cliente pode se conectar ao servidor e interagir com outros usuários.

1. Abra outro terminal para cada cliente que você deseja conectar.
2. Navegue até o diretório onde o arquivo `chat_client.py` está localizado.
3. Execute o cliente com o seguinte comando:

   ```bash
   python chat_client.py
   ```

4. O cliente pedirá para inserir um nome de usuário. Após inserir o nome, o cliente estará pronto para enviar e receber mensagens.

### Passo 3: Trocar Mensagens

- Como cliente, envie uma mensagem ao servidor e espere uma resposta
- Como servidor, permita o usuário se conectar e espere uma mensagem dele(s).
- Após receber uma mensagem, como servidor, é possível responder o cliente com outra mensagem
- O usuário espera resposta do servidor e renderiza no terminal solicitando, em seguida, uma nova mensagem a ser enviada para o servidor repetindo o processo.

## Detalhes Técnicos

- O servidor utiliza o protocolo **UDP** para comunicação. O servidor escuta na porta `5002`.
- O cliente envia as mensagens para o servidor e aguarda pelas respostas.
