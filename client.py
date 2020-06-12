import socket 

# MEDCONNECT was created by Julian Garratt, Aimen Hamed, and Hossion Ali. To run the program use 'python3 server.py'. 
# If 4 or 5 is used while the program is running you should be prompted with '[*] Waiting to connect to patient'.
# At this point run 'python3 client.py' on a seperate terminal. You should then recieve 'Got connection from ...'
# Any issues or bugs please contact Julian Garratt.

# Create a new socket and bind it to the local host under port  10 000, any other port can be used 
# make sure the new port if changed is above 1023 on both programs (0 to 1023 is restricted)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 10000

# Attempt connection to host
try:
    s.connect((host, port))
    s.settimeout(100) #timeout set to 100 seconds
    msg = s.recv(1024)
    print('[*] From the doctor: ' + msg.decode('ascii'))
    s.close()
except socket.timeout:
    print("[*] No connection between client and server or took too long to connect")
    s.close()