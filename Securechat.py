import socket
import threading

# Receive messages
def receive_messages(conn):
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break
            print("\nFriend:", msg)
        except:
            break

# Server
def start_server():
    host = "127.0.0.1"
    port = 12345

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)

    print("Server started. Waiting for connection...")
    conn, addr = server.accept()
    print("Connected with:", addr)

    threading.Thread(target=receive_messages, args=(conn,)).start()

    while True:
        msg = input("You: ")
        conn.send(msg.encode())

# Client
def start_client():
    host = "127.0.0.1"
    port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    print("Connected to server")

    threading.Thread(target=receive_messages, args=(client,)).start()

    while True:
        msg = input("You: ")
        client.send(msg.encode())

# Main
print("Simple Chat Application")
print("1. Start Server")
print("2. Start Client")

choice = input("Enter choice (1 or 2): ")

if choice == "1":
    start_server()
elif choice == "2":
    start_client()
else:
    print("Invalid choice")
