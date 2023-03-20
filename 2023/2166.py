import sys

# https://darkpgmr.tistory.com/86 를 참고함
N = int(input())
arr = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    arr.append((x, y))
arr.append((arr[0][0], arr[0][1]))
area = 0
for i in range(N):
    x = arr[i][0]
    y = arr[i][1]
    x_next = arr[i+1][0]
    y_next = arr[i+1][1]
    area += (x+x_next) * (y-y_next)
area = 0.5 * abs(area)
print(round(area, 1))