import socket

IP = 'localhost'
PORT = 123

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    data = input(">")
    s.sendto(data.encode(), (IP, PORT))
    server_data, addr = s.recvfrom(1024)
    print(bytes.decode(server_data))