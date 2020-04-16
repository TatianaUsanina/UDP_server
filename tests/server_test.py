import time
import unittest
import socket


class server_tests(unittest.TestCase):


    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_wrong_time(self):
            self.failIfEqual(self.get_data(), time.strftime("%H : %M : %S , %d %B %Y", time.localtime()))

    def get_data(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto('time'.encode(), ('localhost', 123))
            data, addr = s.recvfrom(1024)

        return data

if __name__ == "__main__":
    unittest.main()
