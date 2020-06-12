import socket
import sys
import time
import pandas as pd

def main():
    print(r"  __  __        _  ___                      _   ")
    print(r" |  \/  |___ __| |/ __|___ _ _  _ _  ___ __| |_ ")
    print(r" | |\/| / -_) _\` | (__/ _ \ ' \| ' \/ -_) _|  _|")
    print(r" |_|  |_\___\__,_|\___\___/_||_|_||_\___\__|\__|")
    print("\n")

    print("[*] 1 Show clients")
    print("[*] 2 Add patients") #! CHECK
    print("[*] 3 Remove patients")
    print("[*] 4 Send reminder to patient")
    print("[*] 5 Send scheduled reminder to patients")
    print("[*] 6 Exit")

    #get_input()
    add_patient()
    #call_client()

def get_input():
    try:        
        option = int(input("> "))
        if option not in range(1, 7):
            print("[*] Please enter a number from 1 to 5")  
            get_input()
    except ValueError:
        print("[*] Please enter Integers only")
        get_input()
    except KeyboardInterrupt:
        print("\n[*] Exiting")
        sys.exit(1)
    return option

def add_patient():
    name = str(input("Name: "))
    location = str(input("Location: "))
    prescription = str(input("Prescription: "))
    time = str(input("Dose Time: "))
    dose_size = int(input("Dose size: "))

    data = {'Name': [name],
        'Location': [location],
       	'Prescription': [prescription],
       	'Time': [time],
       	'Dose Size': [dose_size]}
    
    try: 
        f = open('patient_data.csv')
        f.close()
    except IOError:
        f = False

    df = pd.DataFrame(data)
    if f != False: df.to_csv('patient_data.csv', mode='a', header=False)
    else: df.to_csv('patient_data.csv', mode='a', header=True)

def call_client():
    host = 'localhost'
    port = 10000
    serversocket = socket.socket()
    serversocket.bind((host, port))
    serversocket.listen(1)
    print("[*] Waiting to connect to client")

    try:
        conn, addr = serversocket.accept()
        print("[*] Got connection from %s" % (str(addr)))
        msg = input() + "\r\n"
        # time.sleep(5)
        conn.send(msg.encode('ascii'))
        conn.close()
    except KeyboardInterrupt:
        print("\n[*] Disconnecting")
        sys.exit(1)


if __name__ == '__main__':
    main()
