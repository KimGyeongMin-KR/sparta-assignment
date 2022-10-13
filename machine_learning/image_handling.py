import torch
import cv2
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

img = cv2.imread('people.jpeg')

results = model(img)
results.save()
#---------세로 x 가로------------#
print(results) # 837x1024
#------------------------------#

result = results.pandas().xyxy[0].to_numpy()
result = [ item for item in result if item[6] == 'person']

tmp_img = cv2.imread('people.jpeg')

for idx,r in enumerate(result):
    cropped = tmp_img[ int(r[1]):int(r[3]) , int(r[0]):int(r[2]) ]
    cv2.imwrite(f'people{idx+1}.png', cropped)

    cv2.rectangle(tmp_img, (int(r[0]), int(r[1])), (int(r[2]), int(r[3])), (255,255,255))
cv2.imwrite('result1.png', tmp_img)
