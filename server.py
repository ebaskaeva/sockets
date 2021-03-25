import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf8'
DISCONNECT_MSG = '!DCN'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_clients(conn, addr):
  print(f'[NEW CONNECTION]: {addr} connected')
  
  connected=True
  while connected:
    msg_lgth=conn.recv(HEADER).decode(FORMAT)
    if msg_lgth:
      msg = conn.recv(int(msg_lgth)).decode(FORMAT)
      print(f'[{addr}]: {msg}')
      if msg == DISCONNECT_MSG:
        connected = False
        print(f'[{addr}]: DISCONNECTED')
  conn.close()


def start():
  server.listen()
  while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_clients, args=(conn, addr))
    thread.start()
    print(f'[ACTIVE CONNECTIONS]: {threading.activeCount()-1}')
    
    
print(f'[Starting] Server starting on {SERVER}.....')
start()    
