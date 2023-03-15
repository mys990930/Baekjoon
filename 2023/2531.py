import sys

N, d, k, c = map(int, sys.stdin.readline().split())
arr = []
for n in range(N):
    arr.append(int(sys.stdin.readline()))

max_cnt = 0
for i in range(len(arr)):
    if i < len(arr) - k + 1:
        dishes = arr[i:i+k]
    else:
        dishes = arr[i:]
        l = k-len(dishes)
        for _ in range(l):
            dishes.append(arr[_])
    temp = {}
    for j in dishes:
        temp[j] = 1
    cnt = len(temp)
    if c not in temp:
        cnt += 1
    if cnt >= max_cnt:
        max_cnt = cnt
print(max_cnt)
