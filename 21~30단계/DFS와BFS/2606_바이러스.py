from collections import deque

c = int(input())
t = int(input())

graph = [ [] for _ in range(c+1)]
count = 0

for i in range(t):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(c+1):
    graph[i].sort()

visited = [ False for _ in range(c+1)]


def bfs(s):
    global count
    que = deque([s])
    visited[s] = True
    while que:
        tmp = que.popleft()
        for i in graph[tmp]:
            if not visited[i]:
                que.append(i)
                visited[i] = True
                count+=1

bfs(1)
print(count)