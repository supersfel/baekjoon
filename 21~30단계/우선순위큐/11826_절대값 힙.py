import sys
import heapq


n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    order = int(sys.stdin.readline())
    if order == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap,[abs(order),order])
