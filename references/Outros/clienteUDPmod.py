# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Cliente de sockets UDP modificado enviar sequencia de mensagens ao servidor
#

# importacao das bibliotecas
from socket import * # sockets
from time import sleep # tempo (opcional)

# definicao das variaveis
serverName = '10.13.0.103' # ip do servidor a se conectar
serverPort = 12000 # porta a se conectar
clientSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP
counter = 0
while 1:
    counter += 1
    print "Enviando para o servidor seq=%d" % (counter)
    clientSocket.sendto(str(counter),(serverName, serverPort)) # envio da mensagem para o servidor
    sleep(1)
clientSocket.close() # encerramento do socket