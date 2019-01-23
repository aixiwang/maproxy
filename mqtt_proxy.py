#!/usr/bin/env python
SSL_MQTT_SERVER_IP = "127.0.0.1"
SSL_MQTT_SERVER_PORT = 8883


import tornado.ioloop
from maproxy.proxyserver import ProxyServer
# HTTP->HTTPS
# "server_ssl_options=True" simply means "connect to server with SSL"

#sl_certs={     "certfile":  "./certificate.pem",
#                "keyfile": "./privatekey.pem" }
# "client_ssl_options=ssl_certs" simply means "listen using SSL"
#server = maproxy.proxyserver.ProxyServer("www.baidu.com",80,
#                                         client_ssl_options=ssl_certs)


server = ProxyServer(SSL_MQTT_SERVER_IP,SSL_MQTT_SERVER_PORT, server_ssl_options=True)
server.listen(1883,address='0.0.0.0')
print("http://0.0.0.0:1883")
tornado.ioloop.IOLoop.instance().start();
