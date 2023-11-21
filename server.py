import socket
from _thread import *
import sys
from player import Player
import pickle

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


players = [Player(0,0,50,50,(255,0,0)), Player(100,100,50,50,(0,255,0))]

def threaded_client(conn, player):
  
  conn.send(pickle.dumps(players[player]))
  reply = ""
  while True:
    try:
      #increase size if truanced errors or something else cringe
      data = pickle.loads(conn.recv(2048))
      players[player] = data


      if not data:
        print("You're disconnected idiot")
        break
      else:
        if player == 1:
          reply = players[0]
        else:
          reply = players[1]
        print("Recieved: ", data)
        print("Sending: ", reply)

      conn.sendall(pickle.dumps(reply))
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