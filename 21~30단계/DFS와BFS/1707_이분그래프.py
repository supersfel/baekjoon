import sys
from collections import deque
input = sys.stdin.readline

k = int(input())

def bfs(start):
    q = deque()
    q.append(start)
    if visited[start] ==0:
        visited[start] = 1
    while q:
        v = q.popleft()

        color = visited[v]
        for i in graph[v]:
            if visited[i] ==0:
                q.append(i)
                if color == 1:
                    visited[i] = 2
                else:
                    visited[i] = 1
            elif visited[i] == color:
                print('NO')
                return
    return True

for _ in range(k):

    v,e = map(int,input().split())
    graph = [[] for __ in range(v+1)]
    visited = [0] * (v+1)

    for __ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    for k in range(1,v+1):
        if not bfs(k):
            break
    else:
        print('YES')

