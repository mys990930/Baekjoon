import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dfs(start_node): # dfs 응용
    global area
    surroundings = get_surrounding_nodes(start_node)
    if arr[start_node.x][start_node.y] == 1:
        arr[start_node.x][start_node.y] = 0
        area += 1
    for node in surroundings:
        if arr[node.x][node.y] == 1:
            dfs(node)

def get_surrounding_nodes(node):
    nodes = []
    if node.x-1 >= 0:
        if arr[node.x - 1][node.y] == 1:
            nodes.append(Node(node.x - 1, node.y))
    if node.x+1 < N:
        if arr[node.x + 1][node.y] == 1:
            nodes.append(Node(node.x + 1, node.y))
    if node.y+1 < M:
        if arr[node.x][node.y + 1] == 1:
            nodes.append(Node(node.x, node.y + 1))
    if node.y-1 >= 0:
        if arr[node.x][node.y - 1] == 1:
            nodes.append(Node(node.x, node.y - 1))
    return nodes

M, N, K = map(int, sys.stdin.readline().split())
arr = [[1]*M for i in range(N)]
areas = []
for j in range(K):
    xmin, ymin, xmax, ymax = map(int, sys.stdin.readline().split())
    x = 0
    y = 0
    for x in range(xmax - xmin):
        for y in range(ymax - ymin):
            arr[xmin + x][ymin + y] = 0

for k in range(N):
    for l in range(M):
        if arr[k][l] == 1:
            area = 0
            dfs(Node(k, l))
            areas.append(area)
areas.sort()
print(len(areas))
for _ in range(len(areas)):
    if _ < len(areas) - 1:
        print(areas[_], end = ' ')
    else: print(areas[_])