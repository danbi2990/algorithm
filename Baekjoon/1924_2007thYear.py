
x, y = map(int, input().split())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
days = y
for i in range(0, x-1):
    days += month[i]
print(day[days % 7])
