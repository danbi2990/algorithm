def isHanNumber(s):
    for i in range(len(s)-2):
        if int(s[i+2]) - int(s[i+1]) != int(s[i+1]) - int(s[i]):
            return False
    return True

N = int(input())
res = 0
for i in range(1, N+1):
    if isHanNumber(str(i)):
        res += 1

print(res)
