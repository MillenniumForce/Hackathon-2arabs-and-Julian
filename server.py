import socket
import sys
import threading
import time
import pandas as pd

def main():
    print(r"  __  __        _  ___                      _   ")
    print(r" |  \/  |___ __| |/ __|___ _ _  _ _  ___ __| |_ ")
    print(r" | |\/| / -_) _\` | (__/ _ \ ' \| ' \/ -_) _|  _|")
    print(r" |_|  |_\___\__,_|\___\___/_||_|_||_\___\__|\__|")
    print("\n")

    print("[1] Show clients") #! DONE
    print("[2] Add patients") #! DONE
    print("[3] Remove patients") #TODO: NOT FUNCTIONAL
    print("[4] Send reminder to patient") #! DONE
    print("[5] Send scheduled reminder to patients") #! DONE
    print("[6] Exit")
    
    user_input = get_input() 
    while (user_input != 6):
        if user_input == 1: show_patient()
        if user_input == 2: add_patient()
        if user_input == 3: remove_patient()
        if user_input == 4: call_client(user_input)
        if user_input == 5: call_client(user_input)
        if user_input == 0: print("[*] Please try again")
        user_input = get_input()
def get_input():
    try:        
        user_input = int(input("> "))
        if user_input not in range(1, 7):
            print("[*] Please enter a number from 1 to 5")  
            return 0
    except ValueError:
        print("[*] Please enter Integers only")
        return 0
    except KeyboardInterrupt:
        print("\n[*] Exiting")
        sys.exit(1)
    except EOFError:
        print("\n[*] Exiting")
        sys.exit(1)
    return user_input

def show_patient():
    try: 
        df = pd.read_csv('patient_data.csv')
        print(df)
    except IOError:
        print("[*] There are no records")
        return
    

def add_patient():
    try:
        first_name = str(input("[*] First Name: "))
        last_name = str(input("[*] Surname: "))
        location = str(input("[*] Location: "))
        prescription = str(input("[*] Prescription: "))
        time = str(input("[*] Dose Time: "))
        dose_frequency = int(input("[*] Dose Frequency (mg): "))
    except KeyboardInterrupt:
        return
    except EOFError: 
        return

    data = {'First Name': [first_name],
        'Surname': [last_name],
        'Location': [location],
       	'Prescription': [prescription],
       	'Time': [time],
       	'Dose Frequency (mg)': [dose_frequency]}
    
    try: 
        f = open('patient_data.csv')
        f.close()
    except IOError:
        f = False

    df = pd.DataFrame(data)
    if f != False: df.to_csv('patient_data.csv', mode='a', index=False, header=False)
    else: df.to_csv('patient_data.csv', mode='a', index=False, header=True)

def remove_patient():
    df = pd.read_csv('patient_data.csv')
    
    try: 
        i = int(input("[*] Enter a number from 0 to %d indicating the row index: " % (len(df)-1)))
        if i not in range(0,len(df)): return 
    except KeyboardInterrupt:
        return
    except EOFError:
        return
    except TypeError:
        return
    df.drop([i,0], inplace = True)


def call_client(user_input):
    host = 'localhost'
    port = 10000
    serversocket = socket.socket()
    try: 
        serversocket.bind((host, port))
        serversocket.listen(1)
    except OSError:
        print("[*] Server is cooling down try again later")
        return
    print("[*] Waiting to connect to patient")

    try:
        conn, addr = serversocket.accept()
        print("[*] Got connection from %s" % (str(addr)))
        if (user_input == 4):
            msg = input("Msg: ") + "\r\n"
            conn.send(msg.encode('ascii'))
            conn.close()
        elif (user_input == 5):
            time_sec = int(input("Enter seconds: "))
            time_min = int(input("Enter minutes: ")) * 60
            time_hours = int(input("Enter hours: ")) * 3600
            user_time = time_sec + time_min + time_hours
            t = threading.Thread(target = scheduled_msg, args = (conn,user_time))
            t.start()
    except KeyboardInterrupt:
        print("\n[*] Disconnecting")
        sys.exit(1)

def scheduled_msg(conn,user_time):
    msg = input("Scheduled Msg: ") + "\r\n"
    time.sleep(user_time)
    conn.send(msg.encode('ascii'))
    conn.close()

if __name__ == '__main__':
    main()
