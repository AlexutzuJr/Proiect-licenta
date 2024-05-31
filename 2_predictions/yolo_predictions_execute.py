import cv2
from yolo_predictions import YOLO_Pred

yolo = YOLO_Pred('./Model/weights/best.onnx', 'data.yaml')

img = cv2.imread('./street_image.jpg')

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_pred = yolo.predictions(img)

cv2.imshow('prediction image', img_pred)
cv2.waitKey(0)
cv2.destroyAllWindows()


# DETECTAREA OBIECTELOR IN TIMP REAL

cap = cv2.VideoCapture('video.mp4')

while True:
    ret, frame = cap.read()
    if ret == False:
        print('nu se poate citi videoclipul')
        break

    pred_image = yolo.predictions(frame)

    cv2.imshow('YOLO', pred_image)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()
