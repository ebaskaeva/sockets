import socket

HEADER = 64
PORT=5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf8'
DISCONNECT_MSG = '!DCN'

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
  m = msg.encode(FORMAT)
  send_lgth=str(len(msg)).encode(FORMAT)
  send_lgth+= b' ' * (HEADER-len(send_lgth))
  client.send(send_lgth)
  client.send(m)
  

def main():
  while True:
    inp = input()
    send(inp)
    if inp == DISCONNECT_MSG:
      send(DISCONNECT_MSG) 
      break
      
      
if __name__ == '__main__':
  main()

