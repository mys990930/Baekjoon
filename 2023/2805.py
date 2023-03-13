import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

min_H = 0
max_H = arr[-1]
H = 0
ans = 0

while min_H <= max_H:
    H = (min_H + max_H) // 2
    tempsum = 0
    for tree in arr:
        if H < tree:
            tempsum += tree - H
    if tempsum >= M: # 가져가려는 나무의 길이보다 더 길게 잘랐다면 절단기 높이를 너무 짧게 잡은 것이므로
        min_H = H + 1 # 중간값보다 더 큰 값을 최소값으로 설정해서 높은 쪽 절반 탐색
        ans = H
    else: max_H = H - 1 # 중간값보다 더 작은 값을 최대값으로 설정해서 낮은 쪽 절반 탐색


print(ans)