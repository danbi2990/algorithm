import sys

read = sys.stdin.readline
n, m = map(int, read().split())
want = []
fence = [-1]*(m+1)

for i in range(n):
    want.append(list(map(int, read().split()))[1:])

def dfs(cow, visited):
    for wish in want[cow]:
        if fence[wish] == -1:
            fence[wish] = cow
            return True
        elif not visited[wish]:
            visited[wish] = True
            old = fence[wish]
            fence[wish] = cow
            if dfs(old, visited):
                return True
    return False

res = 0
for i in range(n):
    visited = [False] * (m + 1)
    if dfs(i, visited):
        res += 1

print(res)
