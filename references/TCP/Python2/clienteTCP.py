# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Cliente de sockets TCP modificado para enviar texto minusculo ao servidor e aguardar resposta em maiuscula
#

# importacao das bibliotecas
from socket import *

# definicao das variaveis
serverName = 'localhost' # ip do servidor
serverPort = 65000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor

sentence = raw_input('Digite o texto em letras minusculas: ')
clientSocket.send(sentence) # envia o texto para o servidor
modifiedSentence = clientSocket.recv(1024) # recebe do servidor a resposta
print 'O servidor (\'%s\', %d) respondeu com: %s' % (serverName, serverPort, modifiedSentence)
clientSocket.close() # encerramento o socket do cliente
