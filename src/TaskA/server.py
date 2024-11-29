####################################################################################################
# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACÃO E AUTOMACÃO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT:
#         - Server: Tarefa A: Desenvolver um sistema de transferência de arquivos
# AUTORES: 
#         - ALUNO 1: Ernane Ferreira Rocha Junior <ernane.junior25@gmail.com> (@ErnaneJ)
#         - ALUNO 2: Quelita Miriam Nunes Ferraz <quelita.miriam.705@ufrn.edu.br> (@Quelita2)
####################################################################################################

import socket
import os

class FileTransferServer:
  """
  Server for handling file transfers.
  """
  SERVER_HOST      = '127.0.0.1'
  SERVER_PORT      = 5001
  BUFFER_SIZE      = 1024
  SERVER_FILES_DIR = './server_files'

  def __init__(self):
    """
    Initializes the server and ensures the server file directory exists.
    """
    os.makedirs(self.SERVER_FILES_DIR, exist_ok=True)
    
    self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server_socket.bind((self.SERVER_HOST, self.SERVER_PORT))
    self.server_socket.listen(5)
    
    print(f"🚀 Server listening on {self.SERVER_HOST}:{self.SERVER_PORT}...")

  def handle_client(self, client_socket, address):
    """
    Handles an individual client connection.

    @param client_socket The client socket object.
    @param address The address of the connected client.
    """
    print(f"🤝 Connection from {address}")
    try:
      while True:
        command = client_socket.recv(self.BUFFER_SIZE).decode()
        if not command:
          break
        args = command.split()
        if len(args) < 2:
          print(f"❌ Invalid command from {address}: {command}")
          client_socket.send(b"Error: Invalid command.\n")
          continue

        action, filename = args[0], args[1]
        filepath = os.path.join(self.SERVER_FILES_DIR, filename)

        if action == "upload":
          try:
            with open(filepath, 'wb') as file:
              data = client_socket.recv(self.BUFFER_SIZE)
              file.write(data)
            print(f"✅ File uploaded by {address}: {filename}")
          except Exception as e:
            print(f"❌ Error during upload by {address}: {e}")
            client_socket.send(f"Error: Error during upload: {e}\n".encode())

        elif action == "download":
          if os.path.exists(filepath):
            try:
              with open(filepath, 'rb') as file:
                client_socket.sendall(file.read())
              os.remove(filepath)
              print(f"✅ File downloaded by {address}: {filename}")
            except Exception as e:
              print(f"❌ Error during download by {address}: {e}")
              client_socket.send(f"Error: Error during download: {e}\n".encode())
          else:
            print(f"❌ File not found on server by {address}: {filename}")
            client_socket.send(b"Error: File not found on server.\n")
        else:
          print(f"❌ Unknown command from {address}: {command}")
          client_socket.send(b"Error: Unknown command.\n")
    except Exception as e:
      print(f"❌ Error with client {address}: {e}")
    finally:
      print(f"👋🏼 Connection with {address} closed.")
      client_socket.close()

  def run(self):
    """
    Runs the server to accept and handle client connections.
    """
    while True:
      client_socket, address = self.server_socket.accept()
      self.handle_client(client_socket, address)

if __name__ == "__main__":
  server = FileTransferServer()
  server.run()