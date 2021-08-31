from socket import *
host = 'localhost'
port = 53
address = (host, port)

while True:
    udpsocket = socket(AF_INET, SOCK_DGRAM)
    request = input("Enter your request: hostname to resolve or ADD hostname address:")
    udpsocket.sendto(str.encode(request), address)
    response = udpsocket.recvfrom(1024)[0].decode()
    print(f"Response: {response}")
