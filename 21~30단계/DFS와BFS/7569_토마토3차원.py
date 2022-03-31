from collections import deque

m,n,h = map(int,input().split())
graph = [ [ list(map(int,input().split())) for _ in range(n) ] for _ in range(h)]
q = deque([])

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] ==1:
                q.append([i,j,k])

dx = [ 0, 1 , 0 , -1 , 0, 0]
dy = [ 1, 0 , -1 , 0 , 0, 0]
dh = [ 0, 0 , 0 , 0 , 1 , -1]

def bfs():
    while q:
        z,x,y = q.popleft()

        for i in range(6):
            nh = z + dh[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nh < h and 0 <= nx < n and 0<= ny < m and graph[nh][nx][ny] ==0:
                q.append([nh,nx,ny])
                graph[nh][nx][ny] = graph[z][x][y] + 1

bfs()
result = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        result = max(result,k)

print(result - 1)

# flag = 0
# result = -2
# for i in range(h):
#     for j in range(n):
#         for k in range(m):
#             # 높이, x,y 순서
#             if graph[i][j][k] == 0:
#                 flag = 1
#                 # 높이, x,y 순서
#             result = max(result,graph[i][j][k])
#
# if flag == 1:
#     print(-1)
# elif result == -1:
#     print(0)
# else:
#     print(result-1)