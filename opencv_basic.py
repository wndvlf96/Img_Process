# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2

img_basic = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)
# imread(file_name, flag) flag는 읽는 방법 설정
# IMREAD_COLOR: 이미지를 컬러로 읽고 투명부분 무시
# IMREAD_GRAYSCALE: 이미지를 Gray_scale로 읽기
# IMREAD_UNCHANGED: 이미지를 컬러로 읽고, 투명한 부분도 읽기(Alpha)
# 반환값은 넘파이 객체로 RGB가 아닌 BGR을 반환

cv2.imshow('img_basic', img_basic)
# 특정 이미지 화면에 출력
# 파이참이 아닐 경우 matplotlib를 이용해서 imshow를 해줘야 합니다.
# 이 때 matplotlib는 RGB순서이므로 BGR2RGB 이런 cvt를 사용해야합니다.

cv2.waitKey(0)              # 이미지 보여주고 바로 꺼지지 않게
# 키보드 입력을 처리하는 함수
# 매개변수로 숫자 받음-> 0은 입력 받을 때 까지 무한대기
# 반환값: 사용자가 누른 것 아스키코드로 반환

cv2.destroyAllWindows()
# 화면의 모든 윈도우를 닫는 함수

img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY)
# 색 바꾸기

cv2.imshow('img_gray', img_gray)
# 특정 이미지 화면에 출력

cv2.waitKey(0)              # 이미지 보여주고 바로 꺼지지 않게
# 키보드 입력을 처리하는 함수
# 매개변수로 숫자 받음-> 0은 입력 받을 때 까지 무한대기
# 반환값: 사용자가 누른 것 아스키코드로 반환

cv2.imwrite('result1.png', img_gray)
# 특정 이미지 파일로 저장하는 함수
# cv.imwrite(file_name, image) image는 저장할 이미지 객체
