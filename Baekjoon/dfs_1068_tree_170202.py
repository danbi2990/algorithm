import sys
read = sys.stdin.readline
n = int(read())
arr = list(map(int, read().split()))
rmv = int(read())

_tree = [[] for _ in range(n)]

rt = -1
for idx, value in enumerate(arr):
    if idx != rmv and value != rmv and value != -1:
        _tree[value].append(idx)
    if value == -1:
        rt = idx

def dfs(idx):
    if len(_tree[idx]) == 0 and arr[idx] != -1:
        return 1

    res = 0
    for child in _tree[idx]:
        res += dfs(child)
    return res

print(dfs(rt))
