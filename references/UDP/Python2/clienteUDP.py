# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Cliente de sockets UDP modificado para enviar texto minusculo ao servidor e aguardar resposta em maiuscula
#

# importacao das bibliotecas
from socket import * # sockets

# definicao das variaveis
serverName = 'localhost' # ip do servidor a se conectar
serverPort = 65000 # porta a se conectar
clientSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP

message = raw_input('Digite o texto em letras minusculas: ')
clientSocket.sendto(message,(serverName, serverPort)) # envia mensagem para o servidor
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) # recebe do servidor a resposta
print 'O servidor (\'%s\', %d) respondeu com: %s' % (serverName, serverPort, modifiedMessage)
clientSocket.close() # encerra o socket do cliente