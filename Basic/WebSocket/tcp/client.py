import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("172.20.10.9",8881))

while True:
    data = input("请输入要发送的数据：")
    client.send(data.encode('utf-8'))

    info = client.recv(1024)
    print(info.decode('utf-8'))