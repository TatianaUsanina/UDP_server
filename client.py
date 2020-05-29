import socket
import datetime
import time
import struct
IP = 'localhost'
PORT = 123



with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
   # FORMAT_DIFF = (datetime.date(1970, 1, 1) - datetime.date(1900, 1, 1)).days * 24 * 3600
    data = b"\x1b" + 39 * b"\0"
    transmit_to_send = time.time()
    data_to_send = data + struct.pack("!II", int(transmit_to_send), int((transmit_to_send - int(transmit_to_send)) * 2 ** 32))
    len(data_to_send)
    s.sendto(data_to_send, (IP, PORT))
    server_data = s.recv(48)
    time_data = struct.unpack('!B B b b 11I', server_data)
    orig = time_data[9] + time_data[10] / 2 ** 32
    recieve_time = time_data[11] + time_data[12] / 2 ** 32
    transmit = time_data[13] + time_data[14] / 2 ** 32
    arrive_time = time.time()
    time_diff = recieve_time - orig - arrive_time + transmit
    print(datetime.datetime.fromtimestamp(time.time() + time_diff).strftime("%c"))
