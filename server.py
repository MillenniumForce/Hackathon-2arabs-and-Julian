import socket
import sys
import time
def main():
    host = 'localhost'
    port = 10000
    serversocket = socket.socket()
    serversocket.bind( (host, port) )
    serversocket.listen(1)
    print("[*] Socket is listening")

    try:
        conn,addr = serversocket.accept()
        print("[*] Got connection from %s" % (str(addr)))
        msg = input() + "\r\n"
        #time.sleep(5)
        conn.send(msg.encode('ascii'))
        conn.close()
    except KeyboardInterrupt:
        print("\n[*] Server shutting down")
        sys.exit(1)
if __name__ == '__main__':
    main()