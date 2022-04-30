import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n= int(input())
m = int(input())
graph = [ [] for _ in range(n+1)]
for _ in range(m):
    s,e,v = map(int,input().split())
    graph[s].append((e,v))

dist = [ [INF] * (n+1) for _ in range(n+1)]
visited = [ [0] *(n+1) for _ in range(n+1)]

for i in range(1,n+1):

    q = [(0,i)]
    while q:
        cnt,node = heapq.heappop(q)

        if dist[i][node] < cnt:
            continue
        if node == i:
            dist[i][node] = 0

        for next,value in graph[node]:
            if dist[i][next] > cnt + value:
                dist[i][next] = cnt + value
                heapq.heappush(q,(cnt+value,next))
                visited[i][next] = node
for i in range(1,n+1):
    for j in range(1,n+1):
        print(dist[i][j] if dist[i][j] != INF else 0,end=' ')
    print()

for i in range(1,n+1):
    for j in range(1,n+1):
        result = [j]
        tmp = visited[i][j]
        while tmp != 0:
            result.append(tmp)
            tmp = visited[i][tmp]
        if len(result)==1:
            print(0)
        else:
            result.reverse()
            print(len(result),*result)
