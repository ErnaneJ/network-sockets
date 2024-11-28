# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Cliente de sockets TCP modificado enviar sequencia de mensagens ao servidor
#

# importacao das bibliotecas
from socket import * # sockets
from time import sleep # tempo (opcional)

# definicao das variaveis
serverName = '10.13.0.103' # ip do servidor
serverPort = 12000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName,serverPort)) # conecta o socket ao servidor
counter = 0
while 1:
    counter += 1
    print "Enviando para o servidor seq=%d" % (counter)
    clientSocket.send(str(counter)) # envia mensagens para o servidor
    sleep(1)
clientSocket.close() # encerramento do socket do cliente