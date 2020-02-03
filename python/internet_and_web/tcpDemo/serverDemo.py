#!/usr/bin/python
# -*- coding: utf-8 -*-

# import socketserver
#
#
# class MyTCPHandler(socketserver.BaseRequestHandler):
#
#     def handle(self):
#         # self.request is the TCP socket connected to the client
#         self.data = self.request.recv(1024).strip()
#         print("{} wrote:".format(self.client_address[0]))
#         print(self.data)
#         # just send back the same data, but upper-cased
#         self.request.sendall(self.data.upper())
#
#
# if __name__ == "__main__":
#     HOST, PORT = "localhost", 9999
#
#     # Create the server, binding to localhost on port 9999
#     with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
#         # Activate the server; this will keep running until you
#         # interrupt the program with Ctrl-C
#         server.serve_forever()




# import socket
# import threading
# import socketserver
#
# class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
#
#     def handle(self):
#         data = str(self.request.recv(1024), 'ascii')
#         cur_thread = threading.current_thread()
#         response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
#         self.request.sendall(response)
#
# class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
#     pass
#
# def client(ip, port, message):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#         sock.connect((ip, port))
#         sock.sendall(bytes(message, 'ascii'))
#         response = str(sock.recv(1024), 'ascii')
#         print("Received: {}".format(response))
#
# if __name__ == "__main__":
#     # Port 0 means to select an arbitrary unused port
#     HOST, PORT = "localhost", 0
#
#     server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
#     with server:
#         ip, port = server.server_address
#
#         # Start a thread with the server -- that thread will then start one
#         # more thread for each request
#         server_thread = threading.Thread(target=server.serve_forever)
#         # Exit the server thread when the main thread terminates
#         server_thread.daemon = True
#         server_thread.start()
#         print("Server loop running in thread:", server_thread.name)
#
#         client(ip, port, "Hello World 1")
#         client(ip, port, "Hello World 2")
#         client(ip, port, "Hello World 3")
#
#         server.shutdown()

import socket

HOST = '127.0.0.4'
PORT = 8000
timeout = 60 * 1   # 1 分钟

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置连接超时
# s.settimeout(2)
s.connect((HOST, PORT))
# 恢复默认超时设置
s.settimeout(None)
s.connect((HOST, PORT))
s.sendall('msg')
