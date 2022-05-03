import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [ [] for _ in range(n+1)]

for _ in range(n-1):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))

def bfs(start):
    q = deque([start])
    visited = [-1] * (n + 1)
    visited[start] = 0
    result = [0, 0]
    while q:
        node = q.popleft()
        for next,w in graph[node]:
            if visited[next] == -1:
                visited[next] = visited[node] + w
                q.append(next)
                if result[1] < visited[next]:
                    result[1] = visited[next]
                    result[0] = next
    return result

node,weight = bfs(1)
node,weight = bfs(node)
print(weight)
