import socket
import subprocess

import struct

sockerServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sockerServer.bind(('127.0.0.1',8080))
while True:
    cmd_bytes,clientAddr = sockerServer.recvfrom(1024)
    cmd = cmd_bytes.decode('utf-8')
    popen = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout_read = popen.stdout.read()
    stderr_read = popen.stderr.read()

    totalSize = len(stderr_read)+len(stdout_read)
    lenth = struct.pack('i', totalSize)
    sockerServer.sendto(lenth,clientAddr)
    sockerServer.sendto(stdout_read,clientAddr)
    sockerServer.sendto(stderr_read,clientAddr)
