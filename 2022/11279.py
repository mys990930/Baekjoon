from collections import deque
import heapq

num = int(input())
q = deque()
heap = []
heapq.heapify(heap)
for i in range(num):
    q.append(int(input()))
for j in range(len(q)):
    temp = q.popleft()
    if temp == 0:
        if len(heap) == 0: print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-temp, temp))