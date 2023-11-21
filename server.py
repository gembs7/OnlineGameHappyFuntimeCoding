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

def read_pos(str):
  str = str.split(",")
  return (float(str[0]), float(str[1]))

def make_pos(tup):
  return str(tup[0]) + "," + str(tup[1])

pos = [(0,0), (100,100)]

def threaded_client(conn, player):
  
  conn.send(str.encode(make_pos(pos[player]))) 
  reply = ""
  while True:
    try:
      #increase size if truanced errors or something else cringe
      data = read_pos(conn.recv(2048).decode())
      pos[player] = data


      if not data:
        print("You're disconnected idiot")
        break
      else:
        if player == 1:
          reply = pos[0]
        else:
          reply = pos[1]
        print("Recieved: ", data)
        print("Sending: ", reply)

      conn.sendall(str.encode(make_pos(reply)))
    except:
      break
  print("Connection Gonzo")
  conn.close()


currentPlayer = 0
while True:
  #accept incoming connections
  conn, addr = s.accept()
  print("One big dog connected to:", addr)

  start_new_thread(threaded_client, (conn, currentPlayer))

  currentPlayer += 1