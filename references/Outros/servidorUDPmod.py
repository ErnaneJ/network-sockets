# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Servidor de sockets UDP modificado para imprimir sequencia de mensagens do cliente
#

# importacao das bibliotecas
from socket import * # sockets

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 12000 # porta a se conectar
serverSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP
serverSocket.bind((serverName, serverPort)) # bind do ip do servidor com a porta
print "Servidor UDP esperando conexoes na porta %d..." % (serverPort)
while 1:
    message, clientAddress = serverSocket.recvfrom(2048) # recebe do cliente
    print "Servidor recebeu seq=%s de %s" % (message, clientAddress)
serverSocket.close() # encerramento do socket