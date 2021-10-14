import io
import socket
import struct
import time
import picamera
import threading
import serial


class PoseClient:
    def __init__(self, port=8000, ip='192.168.86.142') -> None:
        self.client_socket = socket.socket()
        self.client_socket.connect((ip, port))
        self.connection = self.client_socket.makefile('wb')


        try:
            self.camera = picamera.PiCamera()
            self.camera.vflip = True
            self.camera.resolution = (500, 480)
            self.camera.start_preview()
            self.stream = io.BytesIO()
            time.sleep(2)
        except Exception as e:
            print(e)
            self.connection.close()
            self.client_socket.close()


    def sending(self):
        try:
            for _ in self.camera.capture_continuous(self.stream, 'jpeg'):
                self.connection.write(struct.pack('<L', self.stream.tell()))
                self.connection.flush()

                self.stream.seek(0)
                self.connection.write(self.stream.read())
                
                self.stream.seek(0)
                self.stream.truncate()

            self.connection.write(struct.pack('<L', 0))
        except Exception as e:
            self.connection.close()
            self.client_socket.close()



class MessageReceiver:
    def __init__(self, port=8001, ip='192.168.86.142') -> None:
        self.message_socket = socket.socket()
        self.message_socket.connect((ip, port))

        self.ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate
        self.ser.inWaiting()

        self.forward = b"100000000"
        self.backward = b"010000000"
        self.left = b"001000000"
        self.rigth = b"000100000"
        self.stop = b"000010000"    
        self.camera_up = b"000001000"
        self.camera_up = b"000000100"
        self.gripper_close = b"000000010"
        self.gripper_open = b"000000001"

    
    def listening(self):
        data = self.message_socket.recv(1024)
        print(data, type(data), "||",  data.decode('utf-8'), type(data.decode('utf-8')))
        msg = data.decode('utf-8')

        if msg == "left":
            print("left")
            self.ser.write(self.left)

        if msg == "right":
            print("right")
            self.ser.write(self.rigth)

        if msg == "forward":
            print("forward")
            self.ser.write(self.forward)

        if msg == "backward":
            print("backward")
            self.ser.write(self.backward)

        if msg == "stop":
            print("stop")
            self.ser.write(self.stop)


        return self.listening()


    



if __name__ == "__main__":
    ip = "192.168.41.142"
    message_receiver = MessageReceiver(ip=ip)
    task = threading.Thread(target=message_receiver.listening)
    task.start()
    pose_client = PoseClient(ip=ip)
    pose_client.sending()



