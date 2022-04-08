import sys
from collections import deque
input = sys.stdin.readline

INF = int(1e9)
n,m = map(int,input().split())
graph = [ [] for _ in range(n+1)]
visited = [ [] for _ in range(n+1)]

distance = [INF] * (n+1)
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))


def f():
    q = deque()
    q.append((1,0))
    distance[1] = 0
    while q:
        node,cnt = q.popleft()

        if distance[node] < cnt:
            continue

        for i,j in graph[node]:
            if distance[i] > cnt + j:
                if i in visited[node]:
                    return True
                distance[i] = cnt + j
                q.append((i,cnt+j))
                visited[i] += visited[node] + [i]


if f():
    print(-1)
else:
    for i in range(2,n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
