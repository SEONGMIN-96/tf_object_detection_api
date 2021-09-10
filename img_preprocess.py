import cv2
from PIL import Image
import numpy as np
import copy

# image = Image.open('./test_images/test_image_1.jpg')

# src = cv2.imread('./test_images/test_image_0.jpg', cv2.IMREAD_COLOR)
origin = cv2.imread('./test_images/test_image_1.jpg', cv2.IMREAD_COLOR)
# origin = cv2.imread('./test_images/test_image_4.png', cv2.IMREAD_COLOR)
src = copy.deepcopy(origin)
src_g = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

if src is None:
    print('이미지 불러오기 실패...')
else:
    print('이미지 불러오기 성공...')
    # cv2.imshow('src', src)
    cv2.waitKey()
    cv2.destroyAllWindows()

# threshold를 이용하여 binary image로 변환
ret, thresh = cv2.threshold(src_g,127,255,0) # (img, value, value 보다 높을시의 색, value 보다 낮을시의 색)

contours, hier = cv2.findContours(thresh, mode=cv2.RETR_TREE , method=cv2.CHAIN_APPROX_SIMPLE)

image = cv2.drawContours(src, contours, -1, (128,128,128), 3)

# cv2.imshow('origin', origin)
cv2.imshow('contours', image)
cv2.waitKey()
cv2.destroyAllWindows()

############################################################
# 요기까지 객체 테두리의 경계를 잡는 방법
# [Morph] 테두리의 경계에 침식(ERODE)과 팽창(DILATE)를 적용해 테두리를 부각
'''
# 커널생성
kernel = np.ones((2,2), np.uint8)
# para1 : img, para2 : kernel, para3 : epoch
erode = cv2.erode(origin, kernel, iterations=6)
dilate = cv2.dilate(origin, kernel, iterations=6)

# cv2.imshow('origin', origin)
cv2.imshow('erode', erode)
cv2.imshow('dilate', dilate)
cv2.waitKey()
cv2.destroyAllWindows()

# morph opening : 침식 후에 팽창 수행
# morph close : 팽창 후에 침식 수행

# opening
opening1 = cv2.erode(origin, kernel, iterations=3)
opening2 = cv2.dilate(opening1, kernel, iterations=3)

# cv2.imshow('opening', opening2)
# cv2.waitKey()
# cv2.destroyAllWindows()

# close
close1 = cv2.dilate(origin, kernel, iterations=3)
close2 = cv2.erode(close1, kernel, iterations=3)

cv2.imshow('close', close2)
cv2.waitKey()
cv2.destroyAllWindows()

############################################################
# 여기까지 Morph close 실행
# Long Line Remove 실행
# LLR은 불필요한 선을 제거하는 과정.

line = copy.deepcopy(origin)
edges = cv2.Canny(line, 50, 200, apertureSize=3)
gray = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
minLineLength = 120
maxLineGap = 8

lines = cv2.HoughLinesP(edges,1,180/np.pi,150,None,minLineLength,maxLineGap)
for i in range(len(lines)):
    for x1,y1,x2,y2 in lines[i]:
        cv2.line(line,(x1,y1), (x2,y2), (0,255,0),3)

cv2.imshow('line', line)
cv2.waitKey()
cv2.destroyAllWindows()
'''