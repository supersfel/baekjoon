import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    graph = [ [] for __ in range(n+1)]
    visited = [ [INF] * (n+1) for __ in range(2)]
    q = []
    for __ in range(k):
        u,v,c,d = map(int,input().split())
        graph[u].append((v,c,d))

    visited[0][1] = 0
    visited[1][1] = 0
    heapq.heappush(q,(1,0,0))

    while q:

        node,cost,time = heapq.heappop(q)

        if m < cost or visited[1][node] < time:
            continue

        for i,j,k in graph[node]:
            if visited[1][i] > time + k and cost + j <= m:
                visited[0][i] = cost + j
                visited[1][i] = time + k
                heapq.heappush(q,(i,cost + j, time + k))
            elif cost + j <= m:
                heapq.heappush(q,(i,cost + j, time + k))
        print(visited)
    print(visited[1][n] if visited[1][n] != INF else 'Poor KCM')


