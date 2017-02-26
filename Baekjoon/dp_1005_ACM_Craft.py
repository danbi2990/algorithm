t = int(input())

for i in range(t):
    n,k = map(int,input().split())
    d = [0] + list(map(int,input().split()))
    rules = []
    for j in range(k):
        rules.append(tuple(map(int,input().split())))
    w = int(input())

    dp = [0]*(n+1)
    dp[1] = d[1]
    for r in rules:
        dp[r[1]] = max(dp[r[1]], dp[r[0]]+d[r[1]])

    print(dp[w])
