import socket
import struct

sockerClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    cmd = input("请输入命令：").strip()
    sockerClient.sendto(cmd.encode('utf-8'),('127.0.0.1',8080))
    res,serverAddr = sockerClient.recvfrom(4)#4个字节标识服务响应的数据长度
    dataSize = struct.unpack('i',res)[0]
    cmdRes,serverAddr = sockerClient.recvfrom(dataSize)
    print(cmdRes.decode('utf-8'),end='')
