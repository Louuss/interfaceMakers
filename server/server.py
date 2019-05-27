import socket
import sys
import traceback
from threading import Thread

connections = []


def main():
    Thread(target=start_server).start()

    while(1):
        ip = input("ip? ")
        msg = input("msg? ")

        send(ip,msg)

        print("Bien envoye")

def start_server():
    host = "127.0.0.1"
    port = 8888         # arbitrary non-privileged port


    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state, without waiting for its natural timeout to expire
    print("Socket created")

    try:
        soc.bind((host, port))
    except:
        print("Bind failed. Error : " + str(sys.exc_info()))
        sys.exit()

    soc.listen(5)       # queue up to 5 requests
    print("Socket now listening")

    # infinite loop- do not reset for every requests
    while True:
        connection, address = soc.accept()
        ip, port = str(address[0]), str(address[1])
        print("Connected with " + ip + ":" + port)
        connections.append([connection,ip])
        print(connections)
        try:
            Thread(target=client_thread, args=(connection, ip, port)).start()
        except:
            print("Thread did not start.")
            traceback.print_exc()

    soc.close()

def send(ip, msg):
    print(connections)
    for c in connections:
        print(c[1])
        if str(c[1])==ip:
            c[0].send(msg.encode())
            break

def removeConnection(connection):
    for c in connections:
        if c[0]==connection:
            connections.remove(c)
            break

def broadcast(msg):
    for c in connections:
        c[0].send(msg.encode())

def client_input(msg):
    if msg == test:
        print("receivedtest")



def client_thread(connection, ip, port, max_buffer_size = 5120):
    is_active = True

    while is_active:
        client_input = receive_input(connection, max_buffer_size)

        if "--QUIT--" in client_input:
            print("Client is requesting to quit")
            connection.close()
            removeConnection(connection)
            print("Connection " + ip + ":" + port + " closed")
            is_active = False
        else:
            print("Processed result: {}".format(client_input))
            parse(client_input)
            #connection.sendall("-".encode("utf8"))


def receive_input(connection, max_buffer_size):
    client_input = connection.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)

    if client_input_size > max_buffer_size:
        print("The input size is greater than expected {}".format(client_input_size))

    decoded_input = client_input.decode("utf8").rstrip()  # decode and strip end of line
    result = process_input(decoded_input)

    return result


def process_input(input_str):
    print("Processing the input received from client")
#    return "Hello " + str(input_str).upper()
    if input_str == "CMD_VITESSE X" :
        soundEngine()
    elif input_str == "CMD_DEGAT" :
        soundDmg()
    elif input_str == "CMD_TRP":
        soundTorp()
    elif input_str == "CMD_EXP":
        soundExpl()
    elif input_str == "CMD_DEBLOCK":
        unlock()



def unlock():
    for c in connections:
        send(c[1], "CMD_DEBLOCK")

def soundEngine():
    #bruit de moteur
    pass

def soundDmg():
    #bruit de dmg
    pass

def soundTorp():
    #decompte allarmant
    pass

def soundExpl():
    #sond explosion
    pass




if __name__ == "__main__":
    main()
