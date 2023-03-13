import sys

n, m = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))
sum_list = [0 for i in range(n+1)]

for idx in range(n):
    sum_list[idx+1] = sum_list[idx] + num_list[idx]

ans = []

for _ in range(m):
    i, j = map(int, input().split())
    if i == j:
        ans.append(num_list[i-1])
    else:
       ans.append(sum_list[j]-sum_list[i-1])
for t in ans:
    print(t)
