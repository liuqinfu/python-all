import socket

sockerClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sockerClient.connect(("127.0.0.1", 8080))

sockerClient.send('hello world'.encode('utf-8'))
data_bytes = sockerClient.recv(1024)
print("客户端收到消息：",data_bytes.decode('utf-8'))
sockerClient.close()

