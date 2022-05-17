t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    graph = [ [] for __ in range(n+1) ]
    for __ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    tree = [0] * (n+1)
    cnt=0
    tree[1]=1
    for i in range(1,n+1):
        for j in graph[i]:
            if not tree[j]:
                tree[j] =1
                cnt +=1
    print(cnt)