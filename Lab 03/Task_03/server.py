import socket
import threading 
# Get client device name and IP address
port =5050
device_name = socket.gethostname()
server_ip_address = socket.gethostbyname(device_name)

socket_address = (server_ip_address, port)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(socket_address)
server_socket.listen(1)
print(f"Server listening on {server_ip_address}:{port} device name: {device_name}")

def handle_client(client_socket, client_address):
    print(f"Connection established with {client_address}")
    connected = True
    while connected:
        upcoming_message_length = client_socket.recv(15).decode('utf-8')
        print(f"Upcoming message length: {upcoming_message_length}")
        if not upcoming_message_length:
            break
        upcoming_message_length = int(upcoming_message_length.strip())
        message = client_socket.recv(upcoming_message_length).decode('utf-8')
        if message.lower() == "exit":
            print("Client has disconnected.")
            connected = False
            message_to_send = "Goodbye"
        else:
            vowels= 'aeiou'
            count = sum(1 for char in message if char.lower() in vowels)
            if count ==0:
                message_to_send="Not Enough Vowels"
            elif count <= 2:
                message_to_send="Enough vowels I guesss"
            else:
                message_to_send="Too Many Vowels"
            print(f"Message received from client: {message}")
        client_socket.send(message_to_send.encode('utf-8'))
    client_socket.close()



while(True):
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()

