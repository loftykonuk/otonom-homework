import socket
import struct
import time


host = '34.234.82.161'
port = 13571

cn = "lofty"
cn = cn.encode('utf-8')

if len(cn) < 32:
    padding_size = 32 - len(cn)
    padding = b'\x00' * padding_size
    cn += padding

tn = "topic konuk"
tn = tn.encode('utf-8')

if len(tn) < 32:
    padding_size = 32 - len(tn)
    padding = b'\x00' * padding_size
    tn += padding

a = 11
data3 = struct.pack('!I', a)


client_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket1.connect((host, port))
client_socket1.sendall(cn)
client_socket1.sendall(tn)
client_socket1.sendall(data3)

while True:
    client_socket1.sendall("Hello World".encode('utf-8'))
    time.sleep(5)
