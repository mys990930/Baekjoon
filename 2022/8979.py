import sys

N, K = map(int, input().split())
medal_stats = []
for a in range(N):
  medal_stats.append(list(map(int, sys.stdin.readline().split())))
for b in range(N):
  if medal_stats[b][0] == K: break
target = medal_stats[b]

medal_stats.sort(key=lambda x: x[1], reverse=True)
i = 0
while medal_stats[i][1] > target[1]:
  i += 1
j = i
while medal_stats[j][1] == target[1]: #금메달 수 중복인 범위 찾기 위함
  j += 1
  if j >= N: break
silver_medal_stats = medal_stats[i:j]

silver_medal_stats.sort(key=lambda x: x[2], reverse=True)
j = 0
while silver_medal_stats[j][2] > target[2]:
  j += 1
k = j
while silver_medal_stats[k][2] == target[2]:
  k += 1
  if k >= len(silver_medal_stats): break
bronze_medal_stats = silver_medal_stats[j:k]

bronze_medal_stats.sort(key=lambda x: x[3], reverse=True)
k = 0
while bronze_medal_stats[k][3] > target[3]:
  k += 1

print(i+j+k+1)