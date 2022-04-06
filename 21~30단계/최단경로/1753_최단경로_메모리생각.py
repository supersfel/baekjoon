import sys
import heapq
input = sys.stdin.readline

V,e = map(int,input().split())

k = int(input())
INF = int(1e9)
distance = [INF] * (V+1)

graph = [ [] for _ in range(V+1)]


for _ in range(e):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

q = []
heapq.heappush(q,(0,k))
distance[k] = 0
print(graph)

while q:
    print(q)
    cnt,node = heapq.heappop(q)

    print('distance',distance)
    if distance[node] < cnt:
        continue
    for i,j in graph[node]:
        if cnt+j < distance[i]:
            distance[i] = cnt + j
            heapq.heappush(q,(cnt+j,i))


for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])