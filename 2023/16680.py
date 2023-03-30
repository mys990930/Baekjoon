import sys

def is_ansubinsu(n):
    n = str(n)
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if sum % 2 == 1: return True
    else: return False

def print_ansubinsu(n):
    s = str(n)
    temp = int(s + s)
    s = int(n)
    for i in range(99999999):
        ans = temp + s * i
        if is_ansubinsu(ans):
            print(ans)
            break

arr = []
T = int(input())
for i in range(T):
    t = sys.stdin.readline().strip()
    print_ansubinsu(t)