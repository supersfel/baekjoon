import sys
from collections import deque
input = sys.stdin.readline

v = int(input())
graph = [ [] for _ in range(v+1)]
for _ in range(v):
    c = list(map(int, input().split()))
    for e in range(1, len(c) - 2, 2):
        graph[c[0]].append((c[e], c[e + 1]))


def bfs(start):
    visit = [-1] * (v+1)
    q = deque()
    q.append(start)
    visit[start] = 0
    result = [0,0]

    while q:
        node = q.popleft()
        for e,w in graph[node]:
            if visit[e] == -1:
                visit[e] = visit[node] + w
                q.append(e)
                if result[0] < visit[e]:
                    result = [visit[e],e]

    return result

dist , node = bfs(1)
dist , node = bfs(node)
print(dist)