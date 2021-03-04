import numpy as np

# 다차원의 배열을 손쉽게 다룰 수 있음
list_data = [1,2,3,4]
array = np.array(list_data)

print(array)
print(array.size)
print(array.dtype)

# 넘파이의 초기화
arr1 = np.arange(5)
# 0 ~ 매개변수까지 1씩 증가하는 1차원 배열
print(arr1)
arr2 = np.zeros((4,4), dtype=float)
# 특정 크기의 0만 담긴 배열
print(arr2)
arr3 = np.ones((4, 4), dtype=str)
# 특정 크기의 1(문자열의)만 담긴 배열
print(arr3)
arr4 = np.random.randint(0,10,(4,4))
# 0~10까지 랜덤  정수로 넣은 배열
print(arr4)

# 배열 합치기  concatenate
arr5 = np.concatenate([arr2,arr3], axis=1)
# 가로축 합치기
print(arr5)
print(arr5.shape)
arr6 = np.concatenate([arr2,arr3], axis=0)
# 세로축 합치기
print(arr6)
print(arr6.shape)

# 배열 형태 바꾸기  reshape
arr7 = array.reshape((2,2))
print(arr7)

# 배열 나누기  split
# l,r = np.split(array, [k], axis=1) k열을 기준으로 왼쪽을 l, 나머지를 r
larr,rarr = np.split(arr6, [2], axis=1)
print(larr)
print(rarr)

# 단일 객체 저장 및 불러오기
np.save('basic1.npy', arr7)
# 이거는 압축되어 있어서 눌러도 텍스트로 안보임
res1 = np.load('basic1.npy')
print(res1)

# 복수 객체 저장 및 불러오기
np.savez('basic2.npz', array1= larr, array2 = rarr)
res2 = np.load('basic2.npz')
res2_1 = res2['array1']
res2_2 = res2['array2']
print(res2_1)
print(res2_2)

# 원소 정렬(기본은 오름차순)
arr8 = np.array([5,-7,10,5,-80,45])
arr8.sort()
# 리스트랑 동일하게 정렬
print(arr8)
arr8 = arr8[::-1]
# 인덱싱을 통한 정렬
print(arr8)

# 각 열을 정렬
arr9 = np.random.randint(-30,30,(5,5))
print(arr9)
arr9.sort(axis=0)
print(arr9)

# 균일한 간격으로 데이터 생성
arr10 = np.linspace(0,10,5)
print(arr10)

# 넘파이 배열 객체를 복사할때는 .copy()사용하기

# 중복원소 제거 unique(list_name) 사용하기

# 연산
arr11 = np.array([1,2,3,4])
# 리스트와 다르게 연산을 하면 뒤에 생기는게 아니라 스칼라연산
print(arr11*2)
# 또한 브로드캐스트 연산을 통해서 형태가 다른 배열도 연산가능!!!

# 마스킹 연산: 각원소에 대하여 체크해서 T,F 들어감
arr12 = np.arange(16).reshape(4,4)
arr13 = arr12 < 10
print(arr13)
# 마스킹 연산 후 값 바꾸기(이미지 연산에서 중요!)
arr12[arr13] = 100
print(arr12)

# 집계함수
arr14 = np.arange(16).reshape(4,4)
print("max: ", np.max(arr14))
print("min: ", np.min(arr14))
print("sum: ", np.sum(arr14))
print("avg: ", np.mean(arr14))
# 특정 축으로 시행
print('각 열 합: ', np.sum(arr14, axis=0))