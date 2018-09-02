n = int(input())
s = list(map(int, input().split()))
d = [1]*n

for i in range(1,n):
    for j in range(i-1,-1,-1):
        if s[j]<s[i] and d[j]+1>d[i]:
            d[i]=d[j]+1
    # d[i] = 1 + max([d[x] for x in range(i) if s[x] < s[i]])

print(max(d))
