# map 함수
# map(function, iterable)
# 첫번째 매개변수로 함수
# 두번째 매개변수로는 반복 가능한 자료형(리스트, 튜플 등)
chess = [1, 1, 2, 2, 2, 8]
x = list(map(int, input().split()))
for i in range(len(chess)):
    # 끝에 줄바꿈이 아닌 띄어쓰기
    print(chess[i] - x[i], end=' ')