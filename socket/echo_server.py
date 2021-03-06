#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a server example which send hello to client.'

import time, socket, threading

def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    print addr;
    sock.send('Welcome '+str(addr[0])+':'+str(addr[1]))
    #crossdomain = "<cross-domain-policy>" +"<allow-access-from domain='*' to-ports='*' />" +"</cross-domain-policy>" +"\0";
    crossdomain = "<?xml version=\"1.0\"?><!DOCTYPE cross-domain-policy SYSTEM \"http://www.adobe.com/xml/dtds/cross-domain-policy.dtd\"><cross-domain-policy><allow-access-from domain='*' to-ports='*' /></cross-domain-policy>\0";
    while True:
        data = sock.recv(1024)
        print 'msg：'+data
        time.sleep(1)
        if data == 'exit' or not data:
            break
        
        if data.find('policy-file-request') != -1: 
            sock.send(crossdomain)
        else:
            sock.send('Hello, 【%s】 world' % data)
            
    sock.close()
    print 'Connection from %s:%s closed.' % addr

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('127.0.0.1', 9999))
s.listen(5)
print 'Waiting for connection...'
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
