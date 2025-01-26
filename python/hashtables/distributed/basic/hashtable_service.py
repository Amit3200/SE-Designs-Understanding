import sys, os, re, socket, time, mmh3, json
from hashtable import HashTable
from threading import Thread
from datetime import datetime

def connect(ip, port, routes, index):
    connected = False
    while connected is False:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.connect((str(ip), int(port)))
            sock.listen(2)
            routes[index] = sock
            print(f"[Connected to {ip}:{port}] for {index}, {routes}")
            connected = True
        except Exception as e:
            print(e)
            time.sleep(2)



class HashTableService:
    def __init__(self, ip, port, partitions):
        self.ip = ip
        self.port = port
        self.ht = HashTable()
        self.partitions = eval(partitions)
        self.routes = [None]*len(self.partitions)

        for i in range(len(self.partitions)):
            part = self.partitions[i]
            ip, port = part.split(':')
            port = int(port)
            print(i, ip, port)

            if (ip, port) != (self.ip, self.port):
                my_thread = Thread(target=connect, args=(ip, port, self.routes, i, ))
                my_thread.daemon = True
                my_thread.start()

    def handle_commands(self, msg):
        put_ht = re.match('^put ([a-zA-Z0-9]+) ([A-Za-z0-9]+)$', msg)
        get_ht = re.match('^get ([a-zA-Z0-9]+)$', msg)
        remove_ht = re.match('^remove ([a-zA-z0-9]+)$', msg)
        debug_ht = re.match('^debug', msg)
    
        if put_ht:
            key, value = put_ht.groups()
            key_hash = mmh3.hash(key, signed=False) % len(self.partitions)
            if self.routes[key_hash] is None:
                res = self.ht.put(key, value)
                output = "[INSERTED]"
            else:
                self.routes[key_hash].send(msg.encode())
                output = self.routes[key_hash].recv(2048).decode()
        
        elif get_ht:
            key = get_ht.group(1)
            key_hash = mmh3.hash(key, signed=False) % len(self.partitions)
            if self.routes[key_hash] is None:
                res = self.ht.get(key)
                output = res if res is not None else "[ERROR: NON EXISTENT KEY]"
            else:
                self.routes[key_hash].send(msg.encode())
                output = self.routes[key_hash].recv(2048).decode()
        
        elif remove_ht:
            key = remove_ht.group(1)
            key_hash = mmh3.hash(key, signed=False) % len(self.partitions)
            if self.routes[key_hash] is None:
                res = self.ht.remove(key)
                output = "[REMOVED]" if res else "[ERROR: NON EXISTENT KEY]"
            else:
                self.routes[key_hash].send(msg.encode())
                output = self.routes[key_hash].recv(2048).decode()

        else:
            output = "[ERROR: UNKNOWN COMMAND]"
        
        return output

    def process_request(self, conn):
        while True:
            try:
                msg = conn.recv(2048).decode()
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]: {msg} received")
                output = self.handle_commands(msg)
                conn.send(output.encode())
            except Exception as e:
                print("Error processing from client")
                print(e)
    
    def listen_to_clients(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('0.0.0.0', int(self.port)))
        sock.listen(5)

        while True:
            try:
                client_sock, client_address = sock.accept()
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]: New client connected from {client_address}")
                my_thread = Thread(target = self.process_request, args = (client_sock,))
                my_thread.daemon = True
                my_thread.start()
            
            except:
                print("Error accepting connection.....")

if __name__ == "__main__":
    ip_address = str(sys.argv[1])
    port = int(sys.argv[2])
    partitions = str(sys.argv[3])

    dht = HashTableService(ip = ip_address, port = port, partitions = partitions)
    dht.listen_to_clients()
