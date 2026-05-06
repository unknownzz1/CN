import socket

server = socket.socket()
server.bind(("localhost", 12345))
server.listen(1)

print("Server waiting...")

conn, addr = server.accept()
print("Connected to", addr)

while True:
    data = conn.recv(1024).decode()
    print("Client:", data)

    msg = input("You: ")
    conn.send(msg.encode())

    if msg.lower() == "exit":
        break

conn.close()
