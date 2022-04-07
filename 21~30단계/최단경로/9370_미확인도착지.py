import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

T = int(input())
for _ in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    graph = [ [] for __ in range(n+1) ]
    distance =  [INF] * (n+1)
    save = [ False ] * (n+1)
    result = []

    for __ in range(m):
        a,b,d = map(int,input().split())
        graph[a].append([b,d])
        graph[b].append([a,d])
    ends = [ int(input()) for __ in range(t) ]
    ends.sort()

    q = []
    heapq.heappush(q,[s,0])
    distance[s] = 0

    while q:
        node,cnt = heapq.heappop(q)
        if distance[node] < cnt:
            continue
        for j,k in graph[node]:
            if distance[j] >= cnt + k:
                distance[j] = cnt + k
                heapq.heappush(q,[j,cnt+k])

                if (node == g and j == h) or (node == h and j == g) or save[node]:
                    save[j] = True

    for i in ends:
        if save[i]:
            result.append(i)

    print(' '.join(map(str,result)))
