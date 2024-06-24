#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('2-hypermedia_pagination').Server

server = Server()

#print(server.get_hyper(1, 10))
print("---")
#print(server.get_hyper(971, 10))
print("---")
print(server.get_hyper(1942, 10))
print("---")
print(server.get_hyper(1943, 10))
print("---")
print(server.get_hyper(1, 500))
print("---")
#print(server.get_hyper(0, 10))
print("---")
#print(server.get_hyper(-1, 10))
print("---")
#print(server.get_hyper(1, 0))
print("---")
#print(server.get_hyper(1, -10))
print("---")
print(server.get_hyper(1, 20000))
print("---")
#print(server.get_hyper(2, 10))

