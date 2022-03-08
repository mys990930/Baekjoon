import sys

t = int(sys.stdin.readline())
for i in range(t):
    a = sys.stdin.readline().rstrip().split()
    sum = int(a[0]) + int(a[1])
    print(sum)