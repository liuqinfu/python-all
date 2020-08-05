
import socket

socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #重用ip和端口，防止操作系统未及时释放端口而出现的地址被占用
socketServer.bind(('127.0.0.1',8080))
socketServer.listen(5) #5指的是半连接池大小
conn,clientAddr = socketServer.accept()
print('客户端ip和端口：',clientAddr)
data_bytes = conn.recv(1024)
data = data_bytes.decode('utf-8')
print('服务端收到消息：',data)
upper = data.upper()
conn.send(upper.encode('utf-8'))
conn.close()

socketServer.close()

