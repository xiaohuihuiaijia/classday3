import socket
ip_addr = ('www.baidu.com' ,80)
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
sk.connect(ip_addr)
str_request = 'GET / HTTP/1.1\r\n'
str_request += 'Host: www.baidu.com\r\n'
str_request += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n'
str_request += 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36\r\n'
str_request += 'Accept-Language: zh-cn\r\n'
str_request += 'Accept-Encoding: gzip, deflate\r\n'
str_request += 'Connection: keep-alive\r\n'
# str_request += 'keep-alive\r\n'
str_request += '\r\n\r\n'
sk.send(str_request.encode('utf-8'))
while True:
    buf = sk.recv(4*1024,0)
    if not  buf:
        break
    print(buf.decode('utf-8'))


