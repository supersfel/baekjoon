import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
v,e = map(int,input().split())
graph = [ [] for _ in range(v+1) ]

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

dist = [ [INF] * (v + 1) for _ in range(v+1) ]

def f(start):
    #dist[start][start] = 0
    q = []
    heapq.heappush(q,(start,0))

    while q:
        node,cnt = heapq.heappop(q)

        if dist[start][node] < cnt:
            continue
        for i,j in graph[node]:
            if dist[start][i] > cnt + j:
                dist[start][i] = cnt + j
                heapq.heappush(q,(i,cnt+j))

for i in range(1,v+1):
    f(i)
result = INF
for i in range(1,v+1):
    result = min(result,dist[i][i])
print(result if result != INF else -1)