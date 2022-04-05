import sys
from collections import deque
input = sys.stdin.readline

v,e = map(int,input().split())
k = int(input())
INF = int(1e9)
visited = [ INF for _ in range(v+1)  ]
graph = [[] for i in range(v+1)]

for _ in range(e):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

q = deque([[k,0]])

while q:
    node,cnt = q.popleft()

    if cnt > visited[node]:
        continue

    for i,j in graph[node]:
        if visited[i] > cnt + j:
            visited[i] = cnt + j
            q.append((i,visited[i]))

print(0)
for i in range(2,v+2):
    print(visited[i] if visited[i] !=INF else 'INF')



