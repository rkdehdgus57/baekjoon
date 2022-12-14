x1, x2, x3 = list(map(int, input().split()))

if x1 == x2 == x3:
    print(10000 + x1 * 1000)
elif x1 == x2 or x1 == x3:
    print(1000 + x1 * 100)
elif x2 == x3:
    print(1000 + x2 * 100)
elif x1 > x2 and x1 > x3:
    print(x1 * 100)
elif x2 > x1 and x2 > x3:
    print(x2 * 100)
else:
    print(x3 * 100)
