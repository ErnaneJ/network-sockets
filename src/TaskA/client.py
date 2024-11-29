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
import time

class FileTransferClient:
  """
  Client for transferring files to and from a server.
  """
  SERVER_HOST = '127.0.0.1'
  SERVER_PORT = 5001
  BUFFER_SIZE = 1024
  CLIENT_FILES_DIR = './client_files'

  def __init__(self):
    """
    Initializes the client, ensuring the local file directory exists.
    """
    os.makedirs(self.CLIENT_FILES_DIR, exist_ok=True)
    self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.connect_to_server()

  def connect_to_server(self):
    """
    Attempts to connect to the server with retries.
    """
    attempts = 0
    while attempts < 30:
      try:
        self.client_socket.connect((self.SERVER_HOST, self.SERVER_PORT))
        print(f"✅ Connected to server at {self.SERVER_HOST}:{self.SERVER_PORT}")
        return
      except socket.error:
        attempts += 1
        print(f".:: ⏳ Connection attempt {attempts}/30 failed. Retrying in 1 second...")
        time.sleep(1)
    print(".:: ❌ Failed to connect to server. Exiting.")
    exit(1)

  def handle_upload(self, filename):
    """
    Handles uploading a file to the server.

    @param filename Name of the file to upload.
    """
    filepath = os.path.join(self.CLIENT_FILES_DIR, filename)
    if not os.path.exists(filepath):
      print(".:: ❌ File not found in client directory!")
      return

    try:
      print(f".:: ⏳ Uploading {filename} to server...")
      self.client_socket.send(f"upload {filename}".encode())
      with open(filepath, 'rb') as file:
        self.client_socket.sendall(file.read())
      os.remove(filepath)
      print(f".:: ✅ Upload completed successfully.")
    except Exception as e:
      print(f".:: ❌ Error during upload: {e}")

  def handle_download(self, filename):
    """
    Handles downloading a file from the server.

    @param filename Name of the file to download.
    """
    try:
      self.client_socket.send(f"download {filename}".encode())
      response = self.client_socket.recv(self.BUFFER_SIZE)
      if response.startswith(b"Error"):
        print(f".:: ❌ Server error: {response.decode()}")
      else:
        filepath = os.path.join(self.CLIENT_FILES_DIR, filename)
        with open(filepath, 'wb') as file:
          file.write(response)
        print(f".:: ✅ Download completed successfully. File '{filename}' saved to client directory.")
    except Exception as e:
      print(f".:: ❌ Error during download: {e}")

  def run(self):
    """
    Runs the client command loop.
    """
    while True:
      command = input("👉 Enter a command (upload <filename> / download <filename>): ").strip()
      if not command:
        continue
      if command.startswith("upload "):
        self.handle_upload(command.split()[1])
      elif command.startswith("download "):
        self.handle_download(command.split()[1])
      else:
        print(".:: ❌ Invalid command. Please use 'upload <filename>' or 'download <filename>'.")

if __name__ == "__main__":
  client = FileTransferClient()
  client.run()