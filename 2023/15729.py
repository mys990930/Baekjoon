import sys

def onoff(num):
    if num == 1: return 0
    else: return 1

N = int(input())
target = list(map(int, sys.stdin.readline().split()))
buttons = [0 for i in range(N)]

cnt = 0
for i in range(N-2):
    if target[i] != buttons[i]:
        for j in range(i, i+3):
            buttons[j] = onoff(buttons[j])
        cnt += 1

if target [N-2] != buttons[N-2]:
    buttons[N-2] = onoff(buttons[N-2])
    buttons[N-1] = onoff(buttons[N-1])
    cnt += 1
if target[N-1] != buttons[N-1]:
    buttons[N-1] = onoff(buttons[N-1])
    cnt += 1
print(cnt)