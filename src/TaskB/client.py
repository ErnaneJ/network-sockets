####################################################################################################
# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACÃO E AUTOMACÃO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT:
#         - Client - Tarefa B: Desenvolver um sistema de mensagens (bate-papo)
# AUTORES: 
#         - ALUNO 1: Ernane Ferreira Rocha Junior <ernane.junior25@gmail.com> (@ErnaneJ)
#         - ALUNO 2: Quelita Miriam Nunes Ferraz <quelita.miriam.705@ufrn.edu.br> (@Quelita2)
####################################################################################################

import socket

class ChatClient:
  """
  A client for a chat application that communicates with a UDP server.
  """
  SERVER_HOST = '127.0.0.1'
  SERVER_PORT = 5002
  BUFFER_SIZE = 1024

  def __init__(self, client_name):
    """
    Initializes the client with the specified name.

    @param client_name: The name of the client (used for identifying the client in the chat).
    """
    self.client_name = client_name
    self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  def send_message(self):
    """
    Sends a message to the server and waits for a response.
    """
    while True:
      message = input(f"{self.client_name} 💬: ")

      if message.lower() == 'exit':
        print("🚪 Exiting the chat. Goodbye!")
        break

      self.client_socket.sendto(message.encode(), (self.SERVER_HOST, self.SERVER_PORT))
      data, _ = self.client_socket.recvfrom(self.BUFFER_SIZE)
      print(f"🤖 Server: {data.decode()}")

  def run(self):
    """
    Starts the client and handles user input to send messages.
    """
    print(f"🚀 {self.client_name} has joined the chat! Type 'exit' to leave.")
    self.send_message()

if __name__ == "__main__":
  client_name = input("👤 Enter your client name: ")
  client = ChatClient(client_name)
  client.run()
