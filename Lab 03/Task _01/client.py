import socket

# Get client device name and IP address
port =5050
device_name = socket.gethostname()
ip_address = socket.gethostbyname(device_name)
print(f"Device Name: {device_name}, IP Address: {ip_address}")

socket_address = (ip_address, port)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(socket_address)
def sending_message(msg):
    message= msg.encode('utf-8')
    msg_length = len(message)
    msg_length = str(msg_length).encode('utf-8')
    msg_length += b' ' * (15 - len(msg_length)) 
    client_socket.send(msg_length)
    client_socket.send(message)

    sent_from_server= client_socket.recv(128).decode('utf-8')
    print(f"Message from server: {sent_from_server}")

sending_message(f"Hello")

