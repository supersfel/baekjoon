import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
edges = []
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))


def f(start):
    distance[start] = 0

    for i in range(1,n+1):

        for j in range(m):
            s,e,cnt = edges[j]

            if distance[s] != INF and distance[e] > distance[s] + cnt:
                distance[e] = distance[s] + cnt

                if i == n:
                    return True
    return False

if f(1):
    print(-1)
else:
    for i in range(2,n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])