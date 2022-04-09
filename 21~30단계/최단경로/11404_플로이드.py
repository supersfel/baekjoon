import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [ [] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def f(start):
    dist = [INF] * (n+1)
    dist[start] = 0
    q = []
    heapq.heappush(q,(start,0))
    while q:
        node,cnt = heapq.heappop(q)

        if dist[node] < cnt:
            continue

        for i,j in graph[node]:
            if dist[i] > cnt + j:
                dist[i] = cnt + j
                heapq.heappush(q,(i,cnt+j))

    for i in range(1,n+1):
        print(0 if dist[i] == INF else dist[i],end=' ')
    print('')

for i in range(1,n+1):
    f(i)
