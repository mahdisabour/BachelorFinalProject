import cv2
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils



cap = cv2.VideoCapture(0)

while True:
    _ , image = cap.read()
    cv2.imshow("frame",image)
    with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
        #start
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        results = face_detection.process(image)
        #print(results)
        print("after results")
        # Draw the face detection annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.detections:
            for detection in results.detections:
                x = int((detection.location_data.relative_bounding_box.xmin)*640)
                y = int((detection.location_data.relative_bounding_box.ymin)*480)
                w = int((detection.location_data.relative_bounding_box.width)*640)
                h = int((detection.location_data.relative_bounding_box.height)*480)
                
                print(x,y,w,h)
                cv2.circle(image,(x+w//2,y+h//2), 20, (0,0,255), -1)
                mp_drawing.draw_detection(image, detection)
        cv2.imshow('MediaPipe Face Detection', image)


    
    
    k = cv2.waitKey(5)
    if k == ord("q") :
        break

import sys
sys.exit()
