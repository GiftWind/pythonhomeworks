# Написать dns сервер.
# Сервер должен принимать соединения по протоколу udp.
# Если приходит запрос "domain.name" должен отправлять в ответ ip адрес.
# * Доп задание: иметь возможность переопределять записи клиентами:
# * ADD my.google.com:228.228.228.228
from datetime import datetime
from socket import *

# DNS records as a dictionary 
hosts = {}
logfile = 'log.txt'
# Server address
host = 'localhost'
port = 53
address = (host, port)

def log(message):
    print(message)
    with open(logfile, 'a') as f:
        f.write(message)
        f.write("\n")

def serve():
    udpsocket = socket(AF_INET, SOCK_DGRAM)
    udpsocket.bind(address)
    log(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    log("Server started.")
    log("===============")
    while True:
        conn, addr = udpsocket.recvfrom(1024)
        request = conn.decode()
        log(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        log(f"Request from {addr}: {request}")
        if 'ADD' in request:
            request = request.split(" ")
            hostname = request[1]
            newaddress = request[2]
            hosts[hostname] = newaddress
            response = f"address {newaddress} for {hostname} was added"
            udpsocket.sendto(str.encode(response), addr)
            log(f"Add new address {newaddress} for {hostname}")
            log("===============")
        elif request in hosts:
            response = hosts[request]
            udpsocket.sendto(str.encode(response), addr)
            log(f"{request} was in hosts. Send {response} to {addr}")
            log("===============")
        else:
            # If there is no entry for requested hostname
            log(f"{request} was not found in hosts. Resolving...")
            response = gethostbyname(request)
            hosts[request] = response
            log(f"Add record for {request}: {response}")
            udpsocket.sendto(str.encode(response), addr)
            log(f"Send {response} to {addr}")
            log("===============")

if __name__ == '__main__':
    serve()
