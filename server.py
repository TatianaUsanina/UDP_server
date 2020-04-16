import socket
import time
import configparser

def create_configfile(config):
    config['settings'] = {'sec' : 360 }
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
        print("Server is running...")
        while True:
            conn, addr = s.recvfrom(1024)
            data = bytes.decode(conn)
            if data == 'time':
                s.sendto(time.strftime("%H : %M : %S , %d %B %Y", time.localtime(time.time() + sec)).encode(), addr)
            elif data == 'exit':
                break
            else:
                print("Unresolved input")


