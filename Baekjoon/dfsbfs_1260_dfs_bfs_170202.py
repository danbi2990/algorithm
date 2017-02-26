import sys
from collections import deque

read = sys.stdin.readline
n, m, v = map(int, read().split())

graph = [[0]*(n+1) for i in range(n+1)]
visited = [False]*(n+1)
visited2 = [False]*(n+1)

for i in range(m):
    s, t = map(int, read().split())
    graph[s][t] = graph[t][s] = 1

def dfs(vtx):
    print(str(vtx)+' ', end='')
    visited[vtx] = True
    for nxt, exist in enumerate(graph[vtx]):
        if exist and not visited[nxt]:
            dfs(nxt)

def bfs(vtx):
    q = deque()
    q.append(vtx)
    while q:
        curr = q.popleft()
        visited2[curr] = True
        print(str(curr)+' ', end='')
        for nxt, exist in enumerate(graph[curr]):
            if exist and not visited2[nxt]:
                q.append(nxt)
                visited2[nxt] = True

dfs(v)
print()
bfs(v)
