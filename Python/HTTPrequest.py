import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n".encode()
s.send(request)

while True:
  d = s.recv(512)
  if len(d) < 1 :
    break
  print(d.decode())
s.close()
