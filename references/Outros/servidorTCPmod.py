# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Servidor de sockets TCP modificado para imprimir sequencia de mensagens do cliente
#

# importacao das bibliotecas
from socket import * # sockets

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 12000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para "ouvir" conexoes
print "Servidor TCP esperando conexoes na porta %d ..." % (serverPort)
connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
while 1:
    message = connectionSocket.recv(1024) # recebe dados do cliente
    if message == "": 
      break # se algum mensagem vier em branco/vazia, e provavel que o cliente tenha caido, portanto encerra-se o while
    print "Servidor recebeu seq=%s de %s" % (message, addr)
connectionSocket.close() # encerramento do socket do cliente
serverSocket.close() # encerramento do socket do servidor