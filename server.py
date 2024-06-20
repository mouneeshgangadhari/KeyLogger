import socket

HOST = '0.0.0.0'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print(f"Listening on {HOST}:{PORT}")

conn, addr = s.accept()
print('Connected by', addr)

while True:
    data = conn.recv(8000)
    if not data:
        break
    print('Received data:', data.decode())

conn.close()
