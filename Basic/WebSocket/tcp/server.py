import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定端口
server.bind(("172.20.10.9", 8881))

# 监听个数
server.listen(5)
print("服务器启动成功......")

# 等待连接
client_socket, client_address = server.accept()
print("%s----%s 连接成功"%(str(client_address), str(client_socket)))

while True:
    data = client_socket.recv(1024)
    print("收到"+str(client_socket)+"的数据"+data.decode('utf-8'))
    client_socket.send("I recived your message!".encode('utf-8'))


