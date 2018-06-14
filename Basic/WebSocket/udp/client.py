import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input("请输入要发送的信息：")
    client.sendto(data.encode('utf-8'),("172.20.10.9",8787))

    info = client.recv(1024).decode('utf-8')
    print(info)