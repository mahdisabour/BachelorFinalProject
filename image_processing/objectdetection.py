from imageai import Detection
import cv2


modelpath = "./yolo.h5"

yolo = Detection.ObjectDetection()
yolo.setModelTypeAsYOLOv3()
yolo.setModelPath(modelpath)
yolo.loadModel()

cam = cv2.VideoCapture(0) #0=front-cam, 1=back-cam

while True:
    ## read frames
    ret, img = cam.read()
    ## predict yolo
    img, preds = yolo.detectCustomObjectsFromImage(input_image=img, 
                      custom_objects=None, input_type="array",
                      output_type="array",
                      minimum_percentage_probability=70,
                      display_percentage_probability=False,
                      display_object_name=True)
    ## display predictions
    cv2.imshow("object detection", img)
    print(preds)
    ## press q or Esc to quit    
    if (cv2.waitKey(5) & 0xFF == ord("q")):
        break
## close camera
cam.release()
cv2.destroyAllWindows()