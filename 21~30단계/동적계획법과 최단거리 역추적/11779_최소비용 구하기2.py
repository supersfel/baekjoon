import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())
graph = [ [] for _ in range(n+1)]

for _ in range(m):
    s,e,v = map(int,input().split())
    graph[s].append((e,v))
start,end = map(int,input().split())

dist = [ INF for _ in range(n+1) ]
visited = [ 0 for _ in range(n+1)]

q = []
heapq.heappush(q,(0,start))
while q:
    cnt,node = heapq.heappop(q)

    if dist[node] < cnt:
        continue
    if node == start:
        dist[node] = 0

    for next,value in graph[node]:
        if dist[next] > cnt + value:
            dist[next] = cnt + value
            visited[next] = node
            heapq.heappush(q,(cnt+value,next))

print(dist[end])
result = [end]
tmp = visited[end]
while tmp != 0:
    result.append(tmp)
    tmp = visited[tmp]
result.reverse()
print(len(result))
print(*result)
