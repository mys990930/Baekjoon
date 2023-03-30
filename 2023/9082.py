import sys
import math

def solve(n, input):
    arr = list(input[0])
    arr.pop(-1)
    newarr = list(map(int, arr))
    ans = math.ceil(sum(newarr)/3)
    return ans

T = int(sys.stdin.readline())
arr = []
for i in range(T):
    n = int(sys.stdin.readline())
    temp = (str(sys.stdin.readline()), str(sys.stdin.readline()))
    arr.append(solve(n, temp))

for ans in arr:
    print(ans)