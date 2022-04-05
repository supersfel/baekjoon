import sys
from collections import deque
input = sys.stdin.readline

v,e = map(int,input().split())
k = int(input())
visited = [ [ 11 for _ in range(v+1) ] for __ in range(v+1) ]
graph = [[] for i in range(v+1)]

for _ in range(e):
    u,v,w = map(int,input().split())
    visited[u][v] = min(visited[u][v],w)
    graph[u].append(v)

q = deque([[k,0]])
while q:
    node,cnt = q.popleft()
    for i in graph[node]:
        visited[k][i] = min(visited[k][i],cnt + visited[node][i])
        q.append([i,visited[k][i]])

print(0)
for i in range(2,v+2):
    print(visited[k][i] if visited[k][i]<11 else 'INF')



