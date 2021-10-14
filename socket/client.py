from pickle import dumps
import cv2
import numpy as np
import socket
import pickle
import struct
import threading
from time import sleep


def sendData(data, socket_instance):
    print("sending ....")
    # socket_instance.sendall(struct.pack("L", len(data)) + data)
    socket_instance.sendall(data)


def recvData(socket_intance):
    try:
        print("receiving ... ")
        data = socket_intance.recv(1024)
        # print(data)
        return recvData(socket_intance)
    except:
        return None


def main():
    cap=cv2.VideoCapture(0)
    clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clientsocket.connect(('localhost',8089))
    task2 = threading.Thread(target=recvData, args=(clientsocket, ))
    task2.start()
    while True:
        ret,frame=cap.read()
        print(frame)
        data = pickle.dumps(frame)
        sleep(2)
        sendData(data, clientsocket) 




if __name__ == "__main__":
    main()