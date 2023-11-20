import socket
from _thread import *
import sys

server = "192.168.1.7"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.bind((server,port))

except socket.error as e:
  str(e)

# Number of people that can connect
s.listen(2)
print("Waiting for connection, yo")

def threaded_client(conn):
  
  conn.send(str.encode("Connected, honey"))
  reply = ""
  while True:
    try:
      #increase size if truanced errors or something else cringe
      data = conn.recv(2048)
      reply = data.decode("utf-8")

      if not data:
        print("You're disconnected idiot")
        break
      else:
        print("Recieved: ", reply)
        print("Sending: ", reply)

      conn.sendall(str.encode(reply))
    except:
      break
  print("Connection Gonzo")
  conn.close()



while True:
  #accept incoming connections
  conn, addr = s.accept()
  print("One big dog connected to:", addr)

  start_new_thread(threaded_client, (conn,))