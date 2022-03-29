from collections import deque
n,m = map(int,input().split())



miro = [ list(map(int,list(input()))) for _ in range(n)]

dx = [ 0 , 1 , 0 , -1 ]
dy = [ 1 , 0 , -1 , 0 ]
graph = [ [ [] for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        for k in range(4):
            try:
                if miro[i][j] and miro[i+dx[k]][j+dy[k]]:
                    if i+dx[k] >= 0 and j+dy[k] >= 0:
                        graph[i][j].append([i+dx[k],j+dy[k]])
            except:
                continue

q = deque([[0,0,[[0,0]]]])

while q:
    x,y,visited = q.popleft()
    if x == n-1 and y == m-1:
        print(len(visited))
        break
    for a,b in graph[x][y]:
        if not [a,b] in visited:

            q.append([a,b,visited + [[a,b]]])
