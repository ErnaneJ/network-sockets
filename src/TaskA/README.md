# **Sistema de Transferência de Arquivos - Cliente e Servidor**

## **Descrição**

Este é um sistema simples de transferência de arquivos, implementado em Python, utilizando sockets. O sistema permite que um cliente faça upload e download de arquivos para e a partir de um servidor remoto, em uma rede local (localhost). O projeto foi desenvolvido como parte da disciplina de Redes de Computadores (DCA0113) da Universidade Federal do Rio Grande do Norte.

## **Objetivo**

O objetivo do sistema é possibilitar a comunicação entre cliente e servidor para a transferência de arquivos. O cliente pode enviar arquivos para o servidor (upload) e também baixar arquivos do servidor (download). A comunicação é realizada via sockets TCP/IP, com controle básico de erros e confirmações de sucesso ou falha nas operações.

## **Tecnologias**

- Python 3.x
- Sockets (TCP/IP)

## **Requisitos**

- Python 3.x instalado.
- O servidor e o cliente devem estar na mesma rede local (ou ambos rodando na máquina local com o endereço `127.0.0.1`).
- Permissões para ler e escrever arquivos nos diretórios locais.

## **Estrutura do Projeto**

```
/TaskA 
│
├── client.py          # Script do cliente para enviar e receber arquivos.
├── server.py          # Script do servidor para gerenciar as conexões e arquivos.
├── client_files/       # Diretório para armazenar arquivos do cliente.
├── server_files/       # Diretório para armazenar arquivos do servidor.
└── README.md          # Este arquivo.
```

## **Como Executar**

### **0. Se necessário utilize o VENV**

```bash
pwd #=> $PATH/(...)/network-sockets/src/TaskA
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### **1. Executando o Servidor**

1. Abra um terminal.
2. Navegue até o diretório onde o arquivo `server.py` está localizado.
3. Execute o servidor com o comando:
  
   ```bash
   python server.py
   ```

4. O servidor ficará ouvindo por conexões na porta `5001` e aceitará conexões de clientes.

### **2. Executando o Cliente**

1. Abra outro terminal.
2. Navegue até o diretório onde o arquivo `client.py` está localizado.
3. Execute o cliente com o comando:

   ```bash
   python client.py
   ```

4. O cliente tentará se conectar ao servidor. Caso a conexão falhe, ele tentará novamente até o número máximo de 30 tentativas (1 tentativa por segundo).

### **3. Comandos do Cliente**

O cliente pode realizar dois tipos de operações: upload e download de arquivos.

- **Upload de um arquivo**: Para enviar um arquivo do cliente para o servidor, use o comando:

  ```bash
  upload <nome_do_arquivo>
  ```

  Exemplo: `upload shrek.txt`

- **Download de um arquivo**: Para baixar um arquivo do servidor para o cliente, use o comando:

  ```bash
  download <nome_do_arquivo>
  ```

  Exemplo: `download arquivo.txt`

### **4. Comportamento do Sistema**

- Quando o cliente executa um **upload**, o arquivo é enviado para o servidor e removido do diretório do cliente.
- Quando o cliente executa um **download**, o arquivo é baixado do servidor e salvo no diretório do cliente, sendo removido do servidor após o download bem-sucedido.
  
## **Erros e Mensagens**

- **Comandos inválidos**: O sistema verifica se os comandos enviados pelo cliente estão corretos e retorna uma mensagem de erro em caso de falha.
- **Arquivo não encontrado**: Caso o cliente tente enviar ou baixar um arquivo que não existe nos diretórios especificados, uma mensagem de erro será mostrada.
- **Erros de conexão**: Se o cliente não conseguir conectar ao servidor após 30 tentativas, o programa será encerrado com uma mensagem informando a falha de conexão.

## **Exemplo de Uso**

### **Servidor**

Ao iniciar o servidor, ele aguardará as conexões dos clientes:

```bash
🚀 Server listening on 127.0.0.1:5001...
```

### **Cliente**

O cliente tentará se conectar ao servidor:

```bash
.:: ⏳ Connection attempt 1/30 failed. Retrying in 1 second...
```

Após a conexão bem-sucedida, ele pode fazer upload ou download de arquivos:

```bash
👉 Enter a command (upload <filename> / download <filename>): upload arquivo.txt
.:: ⏳ Uploading arquivo.txt to server...
.:: ✅ Upload completed successfully.
```

## **Considerações Finais**

Este projeto foi desenvolvido como parte de um exercício acadêmico para entender os conceitos básicos de redes de computadores e a implementação de um servidor e cliente utilizando sockets. Ele serve como base para sistemas mais complexos que envolvem a troca de arquivos em redes distribuídas.

## **Autoria**

- **Aluno 1**: Ernane Ferreira Rocha Junior - [ernane.junior25@gmail.com](mailto:ernane.junior25@gmail.com)
- **Aluno 2**: Quelita Miriam Nunes Ferraz - [quelita.miriam.705@ufrn.edu.br](mailto:quelita.miriam.705@ufrn.edu.br)