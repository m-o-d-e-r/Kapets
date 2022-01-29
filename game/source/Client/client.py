import threading
import random
import msvcrt
import time
import sys


def events():
    while True:
        print(1)


eventThread = threading.Thread(target = events)
eventThread.start()


def tt():
    while True:
        print(random.random())
        time.sleep(1)


t = threading.Thread(target = tt)
t.start()

"""
    import socket

    address_to_server = ('localhost', 8686)

    USERNAME = input("Username > ")

    while True:
        i_data = input("> ")
        if i_data == "C":
            break
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(address_to_server)
        client.send(f"{USERNAME}___{i_data}".encode("utf-8"))

        data = client.recv(1024)
        print(str(data))

        client.close()
"""