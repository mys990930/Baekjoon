import sys

stack = []
visited = []


def dfs(node): # 재귀로 dfs 구현
    visited.append(node)
    for edge in range(len(arr[node])):
        if arr[node][edge] == 1 and edge not in visited:
            dfs(edge)


N, M = map(int, sys.stdin.readline().split())
arr = [[0]*N for i in range(N)]  # 인접행렬로 그래프 구현
for i in range(M):
    j, k = map(int, sys.stdin.readline().split())
    j -= 1
    k -= 1
    arr[j][k] = 1
    arr[k][j] = 1

comps = 0
for edge in range(len(arr[0])):
    if edge not in visited:
        if 1 in arr[edge]:
            dfs(edge)
            comps += 1
        else: comps += 1
print(comps)
