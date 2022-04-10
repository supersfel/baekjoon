import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    graph = [ [] for _ in range(n+1)]

    for _ in range(k):
        u,v,c,d = map(int,input().split())
        graph[u].append((v,c,d))

    dist = [ [INF] * (m+1) for __ in range(n+1)]
    dist[1][0] = 0
    q = deque([(0,0,1)])

    while q:
        time,cost,node = q.popleft()

        if dist[node][cost] < time:
            continue

        for city,c,t in graph[node]:
            tmp_c = cost + c
            tmp_t = time + t

            if tmp_c <=m and tmp_t < dist[city][tmp_c]:
                for i in range(tmp_c,m+1):
                    if tmp_t < dist[city][i]:
                        dist[city][i] = tmp_t
                    else:
                        break
                q.append((tmp_t,tmp_c,city))

    print( dist[n][m] if dist[n][m] != INF else 'Poor KCM')
