import sys
from collections import deque

read = sys.stdin.readline
neighbor = ((1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1))

while True:
    w, h = map(int, read().split())
    if not w and not h:
        break

    _map = []
    for i in range(h):
        _map.append(list(map(int, read().split(maxsplit=w-1))))

    visited = [[False]*w for x in range(h)]

    res = 0
    for col, lst in enumerate(_map):
        for row, is_land in enumerate(lst):
            q = deque()
            if is_land and not visited[col][row]:
                q.append((col, row))
                res += 1
                while q:
                    cur = q.popleft()
                    visited[col][row] = True
                    for move in neighbor:
                        nxt_y = cur[0] + move[0]
                        nxt_x = cur[1] + move[1]
                        if (0 <= nxt_y < h and 0 <= nxt_x < w
                                and _map[nxt_y][nxt_x] == 1 and not visited[nxt_y][nxt_x]):
                            q.append((nxt_y, nxt_x))
                            visited[nxt_y][nxt_x] = True
    print(res)
