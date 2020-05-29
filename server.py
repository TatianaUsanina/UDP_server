import datetime
import socket
import struct
import time
import configparser
def create_configfile(config):
    config['settings'] = {'sec' : 60 }
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def read_configfile(config):
    return config.get('settings', 'sec')


if __name__ == "__main__":
    PORT = 123
    IP = 'localhost'

    config = configparser.ConfigParser()
    create_configfile(config)
    sec = int(read_configfile(config))
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((IP, PORT))
        print("Сервер запущен")
        conn, addr = s.recvfrom(48)
        receive_time = time.time() + sec
        print(datetime.datetime.fromtimestamp(receive_time).strftime("%c"))
        transmit = conn[40:48]
        orig = transmit
        mode = 4
        first_byte_data = struct.unpack("!B", conn[: 1])
        leap_indicator = first_byte_data[0] >> 6
        version_num = first_byte_data[0] >> 3 & 0b111


        transmit = time.time() + sec
        send_data = struct.pack("!B", (leap_indicator << 6) + (version_num << 3) + mode) \
                    + conn[1 : 24] \
                    + orig \
                    + struct.pack("!2I",
                                  int(receive_time), int((receive_time - int(receive_time)) * 2 ** 32)) \
                    +  struct.pack("!II",
                               int(transmit), int((transmit - int(transmit)) * 2 ** 32))
        s.sendto(send_data, addr)







