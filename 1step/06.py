# map 함수
# map(function, iterable)
# 첫번째 매개변수로 함수
# 두번째 매개변수로는 반복 가능한 자료형(리스트, 튜플 등)
import math

num1, num2 = map(int, input().split())
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)

# trunc 함수는 소수점 아래의 숫자를 버림
print(math.trunc(num1 / num2))
print(num1 % num2)