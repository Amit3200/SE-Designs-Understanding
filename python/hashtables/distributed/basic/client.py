import sys, socket, time
from threading import Thread

def get_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    return sock

if len(sys.argv) != 3:
    print("[CORRECT USAGE]: script, IP address, port number")
    exit()

server_ip_address = str(sys.argv[1])
server_port = int(sys.argv[2])

server = get_socket()
server.connect((server_ip_address, server_port))

def listen_to_messages():
    while True:
        message = server.recv(2048).decode()
        print(message)

t = Thread(target=listen_to_messages)
t.daemon = True
t.start()

request_id = 0

while True:
    command = input("> Input Command:")
    server.send(command.encode())
    request_id += 1
    time.sleep(1)
