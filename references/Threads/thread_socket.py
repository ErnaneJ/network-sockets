# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Exemplo de thread com socket (python 3)
#

# importacao das bibliotecas
from socket import *
import threading

# funcao para receber conexoes dos clientes
def handle_connection(client_socket):
    data = client_socket.recv(1024)
    print(data.decode())
    client_socket.close()

# definicao das variaveis
serverName = '0.0.0.0' # ip do servidor
serverPort = 61000 # porta a se conectar

serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes

print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))

while True:
    connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
    threading.Thread(target=handle_connection, args=(connectionSocket,)).start() # cria thread para cada cliente
