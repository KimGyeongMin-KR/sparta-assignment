import torch
import cv2
import numpy as np
from datetime import datetime, timedelta
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# img = cv2.imread('people.jpeg')

# results = model(img)
# results.save()
# #---------세로 x 가로------------#
# print(results) # 837x1024
# #------------------------------#

# result = results.pandas().xyxy[0].to_numpy()
# result = [ item for item in result if item[6] == 'person']

# tmp_img = cv2.imread('people.jpeg')

# for idx,r in enumerate(result):
#     cropped = tmp_img[ int(r[1]):int(r[3]) , int(r[0]):int(r[2]) ]
#     cv2.imwrite(f'people{idx+1}.png', cropped)

#     cv2.rectangle(tmp_img, (int(r[0]), int(r[1])), (int(r[2]), int(r[3])), (255,255,255))
# cv2.imwrite('result1.png', tmp_img)

# 영상 출력이 아니라 사진 찍듯이 받아내고 처리하기??
def is_study():
    start_time = datetime.now()
    cnt = 0
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        now = datetime.now()
        ret, frame = cap.read()


        if cv2.waitKey(10) & 0xFF == ord('q'):
            print('zz')
            break
        print(ret)
        if cnt % 30 == 0:
            results = model(frame)
            cv2.imshow('YOLO', np.squeeze(results.render()))
            result = results.pandas().xyxy[0].to_numpy()
            result = [ item for item in result if item[6] == 'person']    
            print(result)
        
        # if start_time + timedelta(seconds=5) >= now:
            # break
        cnt+=1
    cap.release()
    cv2.destroyAllWindows()

# is_study()

# 사진 찍듯이 받아내고 처리하기

# def is_study():
#     start_time = datetime.now()

#     cap = cv2.VideoCapture(0)
#     if not cap.isOpened():
#         print("camera open failed")
#         exit()
#     while True:
#         ret, img = cap.read()
#         if not ret:
#             print('cant read camera')
#             break

#         cv2.imshow('px',img)
#         if cv2.waitKey(1) == ord('c'):
#             img_captured = cv2.imwrite('img_captured.png', img)
#         if cv2.waitKey(1) == ord('q'):
#             break
#     cap.release()
#     cv2.destroyAllWindows()

is_study()


# opencv로 웹캠을 제어하고 받는 것이 아니라, 웹페이지에서 사진을 찍고 받아내는 것이 중요해 보인다.