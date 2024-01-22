import socket
import struct
import time


def send(data1, data2, data3):
    client_socket1.sendall(data1)
    client_socket1.sendall(data2)
    client_socket1.sendall(data3)


host = '34.234.82.161'
port = 13571

cn = "lofty"
cn = cn.ljust(32)
tn = "topic konuk"
tn = tn.ljust(32)
a = 1000
data3 = struct.pack('>I', a)


client_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket1.connect((host, port))

while True:
    send(cn, tn, data3)
    time.sleep(5)
