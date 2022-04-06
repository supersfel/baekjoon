import sys
import heapq
input = sys.stdin.readline

n,e = map(int,input().split())
INF = int(1e9)
graph = [ [] for _ in range(n+1)]
distance = [ [INF] * (n+1) for _ in range(n+1) ]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

v1,v2 = map(int,input().split())


for i in [1,v1,v2]:

    q = []
    heapq.heappush(q,[0,i])
    distance[i][i] = 0

    while q:
        cnt,node = heapq.heappop(q)
        if distance[i][node] < cnt:
            continue
        for j,k in graph[node]:
            if cnt + k < distance[i][j]:
                distance[i][j] = cnt + k
                heapq.heappush(q,[cnt+k,j])


result = min(distance[1][v1]+distance[v1][v2]+distance[v2][n],distance[1][v2]+distance[v2][v1]+distance[v1][n])
print(result if result < INF else -1)

