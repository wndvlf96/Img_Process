import cv2

# findContours(image, mode, method)
# 입력 이미지는 Gray Scale Threshold 전처리 과정 필수
# mode: 찾는 방법
# RETR_EXTERNAL: 바깥쪽 Line만 찾기
# RETR_LIST: 모든 line찾지만, 계층을 구성 하지는 않음
# RETR_TREE: 모든 line찾조 계층 구성까지
# method
# CHAIN_APPPROX_NONE: 모든 Contour 포인트 저장
# CHAIN_APPROX_SIMPLE: Contour line을 그릴수 있는 포인트만 저장

# drawContours(image, contours, contours_index, color, thickness)
# contour 그리는 함수
# contour_index: 그리고자 하는 Contour Line(전체: -1)
# 이때 index 0부터 늘려가며 해보면 된다.

img = cv2.imread('cat.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 185,255,0)
# 픽셀의 값이 185보다 큰 경우 255로 바꾸기
cv2.imshow('thresh',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]
img = cv2.drawContours(img, contours, -1, (0,255,0), 4)
cv2.imshow('img',img)
cv2.waitKey(0)

# 사각형 외곽 찾기
ct = contours[0]
x,y,w,h = cv2.boundingRect(ct)
img1 = cv2.rectangle(img, (x,y),(x+w, y+h),(0,0,255),3)
cv2.imshow('img',img1)
cv2.waitKey(0)

# convex Hull 알고리즘
# 대략적인 형태(사각형 -> 다각형)의 Contour 외곽을 빠르게 구할 수 있습니다.(단일 contour 반환)
hull = cv2.convexHull(ct)
img2 = cv2.drawContours(img, [hull], -1, (255,0,0), 4)
cv2.imshow('img',img2)
cv2.waitKey(0)

# contour의 유사 다각형 구하기(엡실론 잘 조정하여서 곡선같은 다각형 만들기)
# approxPolyDP(curve, epsilon, closed) 근사치 contour를 구합니다.
# curve: contour
# epsilon: 최대 거리(클수록 Point 개수 감소)
# closed: 폐곡선 여부
