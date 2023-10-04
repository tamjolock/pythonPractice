import cv2
import numpy as np
import torch

# YOLOv5 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# 클래스 이름 정의
classes = ['person']

# 웹캠 비디오 캡처를 위한 객체 생성
cap = cv2.VideoCapture(0)

# 비디오 캡처 객체가 정상적으로 초기화되었는지 확인
if not cap.isOpened():
    raise IOError("Cannot open webcam")

# 비디오 캡처 루프 시작
while True:
    # 프레임 읽기
    ret, frame = cap.read()

    # 비디오 스트림이 끝나면 루프 종료
    if not ret:
        break

    # YOLOv5를 사용하여 객체 인식 수행
    results = model(frame)

    # 결과에서 객체를 추출하고 바운딩 박스 그리기
    for result in results.xyxy[0]:
        if result[-1] > 0.5 and classes[int(result[5])] == 'person':  # 객체 신뢰도가 0.5보다 크고 클래스가 'person'인 경우
            x1, y1, x2, y2 = result[:4].astype(np.int)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(frame, f'({int((x1+x2)/2)}, {int((y1+y2)/2)})', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # 웹캠 비디오 출력
    cv2.imshow('Webcam', frame)
    
    # 'q'키를 누르면 루프 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 객체 및 창 해제
cap.release()
cv2.destroyAllWindows()