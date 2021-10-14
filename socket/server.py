from os import extsep
import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new
import time
import mediapipe as mp


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

HOST='0.0.0.0'
PORT=8089

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')
conn,addr=s.accept()

### new
data = b""
payload_size = struct.calcsize("L") 
count = 0
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
    while True:
        while len(data) < payload_size:
            print(len(data), "-> len data")
            print(payload_size, "-> payload size")
            print('while 1 ...')
            data += conn.recv(4096)
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("L", packed_msg_size)[0]
        while len(data) < msg_size:
            data += conn.recv(4096)
            try:
                conn.send(b"")
            except:
                conn,addr=s.accept()
                break
        frame_data = data[:msg_size]
        data = data[msg_size:]
        ###

        try:
            image = pickle.loads(frame_data)
            print(image)
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        except Exception as e:
            print("image handle exception")
            print(e)
            continue
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        results = pose.process(image)
        print(image)

        # Draw the pose annotation on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.pose_landmarks is None:
            conn.sendall(b"can't detect anything")
            print("can't detect anything")
            continue
        width, heigth = 500, 480
        # width, heigth = cap.get(3), cap.get(4)
        x = int((results.pose_landmarks.landmark[0].x)*width)
        y = int((results.pose_landmarks.landmark[0].y)*heigth)
        vis = results.pose_landmarks.landmark[0].visibility
        z = results.pose_landmarks.landmark[0].z

        # backward & forward
        if z < -0.9:
            pass
            # print("backward")
        elif -0.9 < z < -0.7:
            pass
            # print("stop")
        elif z > -0.7:
            pass
            # print("forward")

        if x < width // 3:
            pass
            # print("turn left")
        elif width // 3 < x < (width * 2) // 3:
            pass
            # print("without turn")
        elif x > (width * 2) // 3:
            pass
            # print("turn right")
        
        #print(x,y,vis,z)
        cv2.circle(image,(x,y), 10, (0,255,5), -1)
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,)
        cv2.imshow('MediaPipe Pose', image)
        if cv2.waitKey(5) & 0xFF == 27:
          break
        try:
            conn.sendall(b"hello back from server")
        except:
            continue
        