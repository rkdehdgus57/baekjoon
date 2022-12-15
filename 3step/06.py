import sys

n = int(input())

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    z = x + y
    print("Case #" + str(i + 1) + ':', z)
