import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


sk.connect(("www.baidu.com",80))

sk.send(b"GET / HTTP/1.1\r\nHost:www.baidu.com\r\nConnection: close\r\n\r\n")

data = []

while True:
    TempData = sk.recv(1024)
    if TempData:
        data.append(TempData)
    else:
        break

dataStr = (b''.join(data)).decode('utf-8')

sk.close()

print(dataStr)