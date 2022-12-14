x = int(input())
n = int(input())

y = 0
for i in range(n):
    x1, x2 = map(int, input().split())
    y += x1 * x2

if x == y:
    print("Yes")
else:
    print("No")
