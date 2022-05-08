import sys
from collections import deque
input = sys.stdin.readline

def bfs(node):
    q = deque([node])
    flag= True
    while q:
        now = q.popleft()
        if visited[now] == 1:
            flag= False
        visited[now] = 1
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
    return flag



case =1
while True:
    n,m = map(int,input().split())
    if n==0 and m ==0:
        break

    graph = [ [] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (n+1)
    cnt = 0
    for i in range(1,n+1):
        if visited[i] == 1:
            continue
        else:
            if bfs(i):
                cnt +=1
    if cnt == 0:
        print("Case ",case,": No trees.",sep='')
    elif cnt == 1:
        print("Case ",case, ": There is one tree.",sep='')
    else:
        print("Case ",case,": A forest of ",cnt," trees.",sep='')
    case +=1