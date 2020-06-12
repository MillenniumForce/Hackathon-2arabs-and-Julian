import socket
import sys
import threading
import time
import pandas as pd

# MEDCONNECT was created by Julian Garratt, Aimen Hamed, and Hossion Ali. To run the program use 'python3 server.py'. 
# If 4 or 5 is used while the program is running you should be prompted with '[*] Waiting to connect to patient'.
# At this point run 'python3 client.py' on a seperate terminal. You should then recieve 'Got connection from ...'
# Any issues or bugs please contact Julian Garratt.

# Note: pandas is an external library please download via 'python3 -m pip pandas'

def main():
    print(r"  __  __        _  ___                      _   ")
    print(r" |  \/  |___ __| |/ __|___ _ _  _ _  ___ __| |_ ")
    print(r" | |\/| / -_) _\` | (__/ _ \ ' \| ' \/ -_) _|  _|")
    print(r" |_|  |_\___\__,_|\___\___/_||_|_||_\___\__|\__|")
    print("\n")

    print("[1] Show clients") 
    print("[2] Add patients") 
    print("[3] Remove patients") 
    print("[4] Send reminder to patient")  
    print("[5] Send scheduled reminder to patients") 
    print("[6] Exit")

    #Get Input from user
    user_input = get_input()
    while (user_input != 6):
        if user_input == 1: show_patient()
        if user_input == 2: add_patient()
        if user_input == 3: remove_patient()
        if user_input == 4: call_client(user_input)
        if user_input == 5: call_client(user_input)
        if user_input == 0: print("[*] Please try again")
        user_input = get_input()

# Function gets input from user handling exception cases
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

# Calls pandas and prints the dataframe. Note that if the dataframe is large enough it might fill up a substantial part of the terminal
def show_patient():
    try:
        df = pd.read_csv('patient_data.csv')
        if df.empty: print("[*] There are no records")
        else: print(df)
    except IOError:
        print("[*] There are no records")
        return

# Add patients via a pandas dataframe handling exceptions 
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
    except Exception as e:
        print("[?] Incorrect Value due to %s. Please try again\n[?] Note that 'Dose Frequency' must be a number" % (e))
        return

    data = {'First Name': [first_name],
        'Surname': [last_name],
        'Location': [location],
       	'Prescription': [prescription],
       	'Time': [time],
       	'Dose Frequency (mg)': [dose_frequency]}
    
    # Special case where the csv file might not even exist. In that case create a new file instead of appending
    try:
        f = open('patient_data.csv')
        f.close()
    except IOError:
        f = False

    df = pd.DataFrame(data)
    if f != False and df.empty: df.to_csv('patient_data.csv', index=False)
    if f != False: df.to_csv(
        'patient_data.csv', mode='a', index=False, header=False)
    else: df.to_csv('patient_data.csv', mode='a', index=False, header=True)

# Removes patients according to their row index (starts at 0). Might be a bit buggy where in some cases 
# when after all rows are removed it displays 'Unnamed: 0' in the new dataframe
def remove_patient():
    df = pd.read_csv('patient_data.csv')

    if df.empty:
        print("[*] There is nothing to remove")
        return

    try:
        i = int(input(
            "[*] Enter a number from 0 to %d indicating the row index: " % (len(df)-1)))
        if i not in range(0, len(df)): 
            print("[*] Please enter a number within range")
            return
    except KeyboardInterrupt:
        return
    except EOFError:
        return
    except TypeError:
        return

    try: 
        confirm = str(input("[*] Please confirm yes/no if you would like to delete row %d: " % (i)))
        if confirm != 'yes' and confirm != 'no': 
            print("[*] Please enter yes or no to confirm")
            return 
        elif confirm == 'no':
            print("[*] Deletion Cancelled")
            return 
    except KeyboardInterrupt:
        return
    except EOFError:
        return
    except TypeError:
        return

    df.drop(i, inplace = True)
    df.to_csv('patient_data.csv', index=False)

# Function handles all server, socket, and threading
# Will call local host waiting for a connection until client.py is executed
# In built functionality includes either sending a message instantly, or a delayed message using threading
# Cooldown is needed if user tries to run the server to quickly after prior usage
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

# Background process function is called via threading (see call_client() function for implementation)
def scheduled_msg(conn,user_time):
    msg = input("Scheduled Msg: ") + "\r\n"
    time.sleep(user_time)
    conn.send(msg.encode('ascii'))
    conn.close()

if __name__ == '__main__':
    main()
