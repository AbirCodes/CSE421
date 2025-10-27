import socket

port =5050
device_name = socket.gethostname()
server_ip_address = socket.gethostbyname(device_name)

socket_address = (server_ip_address, port)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(socket_address)
server_socket.listen(1)
print(f"Server listening on {server_ip_address}:{port} device name: {device_name}")

while(True):
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")
    connected = True
    while connected:
        upcoming_message_length = client_socket.recv(15).decode('utf-8')
        print(f"Upcoming message length: {upcoming_message_length}")
        if not upcoming_message_length:
            break
        upcoming_message_length = int(upcoming_message_length.strip())
        message = client_socket.recv(upcoming_message_length).decode('utf-8')
        if message == "exit":
            print("Client has disconnected.")
            connected = False
            message_to_send = "Goodbye"
        print(f"Message received from client: {message}")
        message_to_send = f"{message}"
        client_socket.send(message_to_send.encode('utf-8'))
    client_socket.close()