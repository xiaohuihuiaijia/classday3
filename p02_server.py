import socket
ip_addr = ('',)
unix_addr = 'file.socket'
sk = socket.socket(socket.AF_UNIX,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
sk.bind(unix_addr)
while True:
    buf = sk.recv(1024*1,0)
    if  not buf:
        break
    print((buf.decode()))
