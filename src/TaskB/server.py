####################################################################################################
# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACÃO E AUTOMACÃO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT:
#         - Server - Tarefa B: Desenvolver um sistema de mensagens (bate-papo)
# AUTORES: 
#         - ALUNO 1: Ernane Ferreira Rocha Junior <ernane.junior25@gmail.com> (@ErnaneJ)
#         - ALUNO 2: Quelita Miriam Nunes Ferraz <quelita.miriam.705@ufrn.edu.br> (@Quelita2)
####################################################################################################

import socket

class ChatServer:
  """
  A server that handles a UDP-based chat application.
  """
  SERVER_HOST = '127.0.0.1'
  SERVER_PORT = 5002
  BUFFER_SIZE = 1024

  def __init__(self, server_as_a_client=False):
    """
    Initializes the server by creating a UDP socket and binding it to the specified host and port.
    """
    self.users = []
    self.server_as_a_client = server_as_a_client
    self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.server_socket.bind((self.SERVER_HOST, self.SERVER_PORT))

  def handle_client(self):
    """
    Receives a message from the client, prints it, and sends a response back.
    """
    while True:
      data, addr = self.server_socket.recvfrom(self.BUFFER_SIZE)
      print(f"🗣️ Message received from {addr}: {data.decode()}")
      
      response = input(f"👨‍💻 Server: Type your response to {addr}: ")

      if response.lower() == 'exit':
        print("🚪 Exiting the chat. Goodbye!")
        break

      self.server_socket.sendto(response.encode(), addr)

  def run(self):
    """
    Runs the server to handle incoming client messages.
    """
    print(f"🚀 Server listening on {self.SERVER_HOST}:{self.SERVER_PORT}...")
    self.handle_client()

if __name__ == "__main__":
  server = ChatServer(server_as_a_client=False)
  server.run()