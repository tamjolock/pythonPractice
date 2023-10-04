{설치해야할 모듈}
(명령어)
pip install seaborn
pip install gitpython scipy setuptools 
pip install matplotlib 
pip install tqdm 
pip install psutil 
pip install pyyaml 
pip install pandas
pip install torch torchvision 




1.필요한 라이브러리와 모듈을 import합니다.

cv2: OpenCV 라이브러리
numpy: 수치 계산 라이브러리
torch: PyTorch 라이브러리
time: 시간 관련 라이브러리
YOLOv5 모델을 로드합니다.

2.ultralytics/yolov5 저장소에서 'yolov5s' 모델을 pretrained=True 옵션으로 로드합니다.
클래스 이름을 정의합니다.

3.COCO 데이터셋의 클래스 이름을 정의합니다.
웹캠 비디오 캡처를 위한 객체를 생성합니다.

4.cv2.VideoCapture() 함수를 사용하여 웹캠 장치의 비디오 캡처 객체를 생성합니다.
비디오 캡처 객체가 정상적으로 초기화되었는지 확인합니다.

5.isOpened() 함수를 사용하여 비디오 캡처 객체가 초기화되었는지 확인합니다.
객체가 초기화되지 않은 경우 raise IOError로 예외를 발생시킵니다.
비디오 캡처 루프를 시작합니다.

6.while 문을 사용하여 비디오 프레임을 계속 읽어옵니다.
프레임을 읽습니다.

7.cap.read() 함수를 사용하여 비디오 프레임을 읽어옵니다.
비디오 스트림이 끝나면 루프를 종료합니다.

8.ret 변수가 False인 경우 while 루프를 종료합니다.
YOLOv5를 사용하여 객체 인식을 수행합니다.

9.model() 함수를 사용하여 프레임에서 객체 인식을 수행합니다.
결과에서 객체를 추출하고 바운딩 박스를 그립니다.

10.results.xyxy[0]을 사용하여 각 객체의 위치와 신뢰도를 추출합니다.
결과에서 객체 신뢰도가 0.5 이상인 객체의 경우 바운딩 박스와 객체의 클래스 이름을 표시합니다.
웹캠 비디오를 출력합니다.

11.cv2.imshow() 함수를 사용하여 웹캠 비디오를 출력합니다.
'q'키를 누르면 루프를 종료합니다.

12.cv2.waitKey() 함수를 사용하여 키 이벤트를 대기합니다.
키 이벤트가 'q'인 경우 while 루프를 종료합니다.
객체 및 창을 해제합니다.

13.cap.release() 함수를 사용하여 비디오 캡처 객체를 해제합니다.
cv2.destroyAllWindows() 함수를 사용하여 모든 창을 닫습니다.


#시작
import cv2
import numpy as np
import requests
import urllib.request
from io import BytesIO
import time
import torch

# YOLOv5 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model.conf = 0.4  # confidence threshold
model.iou = 0.5  # NMS IoU threshold

# ESP32-CAM으로부터 이미지 가져오기
def get_image():
    img_resp = requests.get("http://192.168.1.201/capture", stream=True, timeout=5)
    img = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img, -1)
    return img

# 윈도우 창 초기화
cv2.namedWindow("Object Detection", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Object Detection", 800, 600)

while True:
    # ESP32-CAM으로부터 이미지 가져오기
    img = get_image()

    # YOLOv5 모델을 사용하여 객체 감지
    results = model(img)

    # 객체 인식 결과를 화면에 그리기
    for result in results.xyxy[0]:
        class_id = int(result[5])
        class_name = model.names[class_id]
        confidence = float(result[4])
        bbox = result[:4]

        # 박스 그리기
        pt1 = (int(bbox[0]), int(bbox[1]))
        pt2 = (int(bbox[2]), int(bbox[3]))
        cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)

        # 클래스 이름과 신뢰도 점수 그리기
        label = f'{class_name} {confidence:.2f}'
        cv2.putText(img, label, pt1, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # 화면에 이미지 보여주기
    cv2.imshow("Object Detection", img)

    # 'q'키를 누르면 종료
    if cv2.waitKey(1) == ord('q'):
        break

# 자원 해제
cv2.destroyAllWindows()