n = int(input())

map = [ list(map(int,list(input()))) for _ in range(n) ]

graph = [[[] for _ in range(n)] for __ in range(n)]
visited = [ [False] * n for _ in range(n) ]
result = []
count = 1

dx = [0,1,0,-1]
dy = [1,0,-1,0]


for i in range(n):
    for j in range(n):
        for k in range(4):
            try:
                if  map[i][j] and map[i+dx[k]][j+dy[k]]:
                    if i+dx[k]>=0 and j+dy[k]>=0:
                        graph[i][j].append([i+dx[k],j+dy[k]])
            except:
                continue

def dfs(i,j):
    global count
    visited[i][j] = True
    for x,y in graph[i][j]:
        if not visited[x][y]:
            dfs(x,y)
            count +=1

for i in range(n):
    for j in range(n):
        if not visited[i][j] and map[i][j]:
            count = 1
            dfs(i,j)
            result.append(count)


result.sort()

print(len(result))
for i in result:
    print(i)





