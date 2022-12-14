num1, num2 = map(int, input().split())

m = num2 - 45

if m < 0:
    y = num1 - 1
    if y < 0:
        print(23, num2 + 15)
    else:
        print(num1 - 1, num2 + 15)
else:
    print(num1, num2 - 45)
