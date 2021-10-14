import cv2


cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    # cv2.imshow('MediaPipe Pose', frame)
    print(len(frame))
    # if cv2.waitKey(5) & 0xFF == 27:
    #     break
