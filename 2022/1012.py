import sys
sys.setrecursionlimit(10**6)
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dfs(start_node): # dfs 응용
    surroundings = get_surrounding_nodes(start_node)
    arr[start_node.x][start_node.y] = 0
    for node in surroundings:
        dfs(node)

def get_surrounding_nodes(node):
    nodes = []
    if node.x-1 >= 0:
        if arr[node.x - 1][node.y] == 1:
            nodes.append(Node(node.x - 1, node.y))
    if node.x+1 < M:
        if arr[node.x + 1][node.y] == 1:
            nodes.append(Node(node.x + 1, node.y))
    if node.y+1 < N:
        if arr[node.x][node.y + 1] == 1:
            nodes.append(Node(node.x, node.y + 1))
    if node.y-1 >= 0:
        if arr[node.x][node.y - 1] == 1:
            nodes.append(Node(node.x, node.y - 1))
    return nodes

worms = []
case_num = int(input())
for num in range(case_num):
    M, N, K = map(int, sys.stdin.readline().split())
    i = 0
    arr = [[0]*N for i in range(M)]
    cabbage_nodes = []
    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        arr[x][y] = 1
        node = Node(x, y)
        cabbage_nodes.append(node)
    comps = 0
    for coordinate in cabbage_nodes:
        if arr[coordinate.x][coordinate.y] == 1:
            dfs(coordinate)
            comps += 1
    worms.append(comps)

for i in range(len(worms)):
    print(worms[i])
