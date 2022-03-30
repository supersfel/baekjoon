t = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for _ in range(t):
    m,n,k = map(int,input().split())

    farm = [ [ 0 for _ in range(m) ] for __ in range(n) ]
    graph = [[[] for _ in range(m)] for __ in range(n)]
    visited = [ [False] * m for _ in range(n) ]
    cnt = 0


    for __ in range(k):
        x,y = map(int,input().split())
        farm[y][x] = 1

    for i in range(n):
        for j in range(m):
            for k in range(4):
                try:
                    if farm[i][j] and farm[i+dx[k]][j+dy[k]]:
                        if i + dx[k] >= 0 and j + dy[k] >= 0:
                            graph[i][j].append([i+dx[k],j+dy[k]])
                except:
                    continue

    def dfs(x,y):
        visited[x][y] = True

        for a,b in graph[x][y]:
            if not visited[a][b]:
                dfs(a,b)

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and farm[i][j]:
                dfs(i,j)
                cnt+=1

    print(cnt)