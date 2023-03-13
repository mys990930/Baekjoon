import sys

N, C = map(int, sys.stdin.readline().split())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline().strip()))
arr.sort()

min_gap = 1
max_gap = arr[-1] - arr[0]
result = 0

while min_gap <= max_gap:
    gap = (min_gap + max_gap) // 2
    cnt = 1
    tmp = arr[0]
    for n in range(len(arr)): # arr[0]부터 gap만큼 더해주면서 총 공유기 cnt 세기
        if arr[n] >= tmp + gap:
            tmp = arr[n]
            cnt += 1
    if cnt >= C:
        min_gap = gap + 1 # 중간값보다 더 큰 값을 최소값으로 설정해서 높은 쪽 절반 탐색
        result = gap
    else: max_gap = gap - 1 # 중간값보다 더 작은 값을 최대값으로 설정해서 낮은 쪽 절반 탐색

print(result)