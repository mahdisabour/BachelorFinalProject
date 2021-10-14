import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


cap = cv2.VideoCapture(0)

with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        results = pose.process(image)

        # Draw the pose annotation on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.pose_landmarks is None:
            print("continue")
            continue
        width, heigth = cap.get(3), cap.get(4)
        x = int((results.pose_landmarks.landmark[0].x)*width)
        y = int((results.pose_landmarks.landmark[0].y)*heigth)
        vis = results.pose_landmarks.landmark[0].visibility
        z = results.pose_landmarks.landmark[0].z
        print(z)

        # backward & forward
        if z < -0.9:
            print("backward")
        elif -0.9 < z < -0.7:
            print("stop")
        elif z > -0.7:
            print("forward")

        print(x, y)
        if x < width // 3:
            print("turn left")
        elif width // 3 < x < (width * 2) // 3:
            print("without turn")
        elif x > (width * 2) // 3:
            print("turn right")
        
        
        #print(x,y,vis,z)
        cv2.circle(image,(x,y), 10, (0,255,5), -1)
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,)
        # cv2.imshow('MediaPipe Pose', image)
        # if cv2.waitKey(5) & 0xFF == 27:
        #   break
cap.release()