import sys
read = sys.stdin.readline
n = int(read())
arr = tuple(map(int, read().split()))
d = [0]*1001

res = d[arr[0]] = arr[0]
for i in range(1,n,1):
    d[arr[i]] = max([d[arr[x]] for x in range(i+1) if arr[x] <= arr[i]]) + arr[i]
    res = d[arr[i]] if d[arr[i]] > res else res

print(res)
