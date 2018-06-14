import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("172.20.10.9",8787))

while True:
    info, addr = server.recvfrom(1024)
    print("client say:"+info.decode('utf-8'))

    data = input("Please input your data to send:")
    server.sendto(data.encode('utf-8'),addr)

