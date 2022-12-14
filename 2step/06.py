hour, minute1 = map(int, input().split())
minute2 = int(input())

minute = minute1 + minute2

if minute // 60 != 0:
    hour = hour + (minute // 60)
    minute = minute - (minute // 60 * 60)

if hour >= 24:
    hour = hour - 24

print(hour, minute)
