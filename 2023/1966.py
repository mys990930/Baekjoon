import sys
import copy
from collections import deque

class Document:
    def __init__(self, num):
        self.priority = num

def solve(N, position, priorities):
    q = deque()
    cnt = 0

    for i in priorities:
        q.append(i)

    while True:
        for doc in copy.deepcopy(q):
            if doc >= max(q): # if document is prior to others
                q.popleft() # doc printed
                cnt += 1
                if position == 0:
                    return cnt
                else:
                    position -= 1
            else:
                if position == 0:
                    temp = q.popleft()
                    position = len(q)
                    q.append(temp)
                else:
                    temp = q.popleft()
                    position -= 1
                    q.append(temp)

tests = int(input())
ans = []
for i in range(tests):
    N, M = map(int, sys.stdin.readline().split())
    priorities = list(map(int, sys.stdin.readline().split()))
    ans.append(solve(N, M, priorities))

for _ in range(len(ans)):
    print(ans[_])