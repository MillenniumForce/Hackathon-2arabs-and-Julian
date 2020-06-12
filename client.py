import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 10000

try:
    s.connect((host, port))
    msg = s.recv(1024)
    print('[*] From the doctor ' + msg.decode('ascii'))
    s.close()
except socket.timeout:
    print("[*] No connection between client and server")
    s.close()