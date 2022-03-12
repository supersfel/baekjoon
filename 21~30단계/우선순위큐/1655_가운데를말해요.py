import sys
import heapq

n = int(sys.stdin.readline())
min_heap = []
max_heap = []


for _ in range(n):
    num = int(sys.stdin.readline())

    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap,-num)
    else:
        heapq.heappush(min_heap,num)


    if  len(max_heap)>=1 and len(min_heap)>=1 and min_heap[0] < max_heap[0] * -1:
        min_tmp = heapq.heappop(min_heap)
        max_tmp = heapq.heappop(max_heap) * -1

        heapq.heappush(min_heap,max_tmp)
        heapq.heappush(max_heap,min_tmp *-1)

    print(max_heap[0] * -1)




