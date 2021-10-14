import io
import socket
import struct
from PIL import Image
import cv2
import numpy
import mediapipe as mp
from numpy.core.numeric import extend_all
from message_broker import MessageBrokerServer




class PoseServer:
    def __init__(self, port=8000) -> None:
        self.server_socket = socket.socket()
        self.server_socket.bind(('0.0.0.0', port))
        self.server_socket.listen(0)
        # setup mediapipe
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.width, self.heigth = 500, 480
        self.message_broker = MessageBrokerServer()
        self.move = None
        self.turn = None
        self.stop = None
        self.setupConnection()


    def setupConnection(self):
        self.connection = self.server_socket.accept()[0].makefile('rb')
        self.listening()

    
    def listening(self):
        try:
            while True:
                # Read the length of the image as a 32-bit unsigned int. If the
                # length is zero, quit the loop
                image_len = struct.unpack('<L', self.connection.read(struct.calcsize('<L')))[0]
                if not image_len:
                    break

                # Construct a stream to hold the image data and read the image
                # data from the connection
                image_stream = io.BytesIO()
                image_stream.write(self.connection.read(image_len))

                # Rewind the stream, open it as an image with PIL and do some
                # processing on it
                image_stream.seek(0)
                image = Image.open(image_stream)
                opencvImage = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
                image = self.poseDetection(opencvImage)
                if image is None:
                    image = opencvImage

                self.showCV(image)
                if cv2.waitKey(5) & 0xFF == 27:
                    print("close")
                    self.message_broker.conn.close()
                    self.connection.close()
                    break
        except Exception as e:
            print(e)
            self.message_broker.connect()
            self.setupConnection()


    
    def poseDetection(self, image):
        image.flags.writeable = False
        results = self.pose.process(image)
        image.flags.writeable = True
        # self.estimateMovement(0, 0)
        if results.pose_landmarks is None:
            self.estimateMovement(None, None, None)
            return None
        x = int((results.pose_landmarks.landmark[0].x)*self.width)
        y = int((results.pose_landmarks.landmark[0].y)*self.heigth)
        # vis = results.pose_landmarks.landmark[0].visibility
        z = results.pose_landmarks.landmark[0].z
        self.estimateMovement(x, y, z)
        cv2.circle(image,(x,y), 10, (0,255,5), -1)
        self.mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            self.mp_pose.POSE_CONNECTIONS,)
        return image

    
    def estimateMovement(self, x, y, z):

        # if camera can not detect anybody
        if x == None and z == None and y == None:
            self.checkMovement(move="stop")
            return

        move = None
        # turn = None
        # stop = None
        # print("x -> ", x)
        # print("width -> ", self.width)
        # # print("z -> ", z)
        # # print("y -> ", y)

        # if x < self.width // 3:
        #     print("rigth", "1")
        #     turn = "rigth"
        # elif x > (self.width * 2) // 3:
        #     turn = "left"


        # if y < 120:
        #     move = "backward"
        # elif y > 150:
        #     move = "forward"
        # else:
        #     stop = "stop"

        if x < (self.width // 3):
            move = "right"
        elif x > ((self.width * 2) // 3):
            move = "left"
        elif y < 100:
            move = "backward"
        elif y > 150:
            move = "forward"
        else:
            move = "stop"
        
        self.checkMovement(move)

        # self.checkMovement(move, turn, stop)

    
    def checkMovement(self, move):
        if move != self.move:
            self.message_broker.send(move)
            self.move = move


    # def checkMovement(self, move, turn, stop):

    #     if turn != self.turn and turn:
    #         print(turn, "2")
    #         self.message_broker.send(turn)
    #         self.turn = turn
    #         return


    #     elif stop != self.stop:
    #         if stop == "stop":
    #             self.message_broker.send("stop")
    #             self.stop = stop
    #             return
    #         self.stop = stop


    #     elif move != self.move and move:
    #         self.message_broker.send(move)
    #         self.move = move
    #         return


    def showCV(self, opencvImage):
        cv2.imshow('MediaPipe Pose', opencvImage)

    
    def closeConnection(self):
        self.connection.close()
        self.server_socket.close()



if __name__ == "__main__":
    pose_server = PoseServer()




    

