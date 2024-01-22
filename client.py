import socket
import struct
import time


host = '34.234.82.161'
port = 13571

client_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket1.connect((host, port))

cn = "lofty"
cn = cn.ljust(32)
tn = "topic konuk"
tn = tn.ljust(32)
a = 1000
message1 = cn.encode('utf-8') + tn.encode('utf-8') + struct.pack('!I', a)

while True:
    client_socket1.sendall(message1)
    time.sleep(5)
