import time
import cv2
import numpy as np
import math
import serial

# ESP32 카메라 모듈을 사용하여 비디오 캡처를 시작합니다.
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# YOLOv5 객체 인식 모델을 로드합니다.
net = cv2.dnn.readNet("yolov5.weights", "yolov5.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# 라이다 센서와의 시리얼 통신을 시작합니다.
ser = serial.Serial('/dev/ttyUSB0', 9600)

# 무한 반복을 시작합니다.
while True:
    # 프레임을 캡처합니다.
    ret, frame = cap.read()

    # YOLOv5 객체 인식을 수행합니다.
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416,416), (0,0,0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * frame.shape[1])
                center_y = int(detection[1] * frame.shape[0])
                w = int(detection[2] * frame.shape[1])
                h = int(detection[3] * frame.shape[0])
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # 인식된 객체를 그립니다.
    font = cv2.FONT_HERSHEY_SIMPLEX
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            cv2.rectangle(frame, (x,y), (x+w,y+h), color, 2)
            cv2.putText(frame, label, (x,y+30), font, 1, color, 2)

    # 라이다 센서 값 읽기
    lidar_data = ser.readline().decode('ascii').strip()

    # 라이다 센서 값을 통해 거리를 계산합니다.
    distance = int(lidar_data)

    # 거리 값을 화면에 출력합니다.
    cv2.putText(frame, "Distance: {} cm".format(distance), (10, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # 화면에 출력된 이미지를 보여줍니다.
    cv2.imshow("Image", frame)

    # q 키를 누르면 루프를 중단합니다.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cap.release()
    cv2.destroyAllWindows()
    ser.close()