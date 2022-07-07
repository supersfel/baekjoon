import sys
from collections import deque
import math
input = sys.stdin.readline

n,l,r = map(int,input().split())
city = [ list(map(int,input().split())) for _ in range(n)]


dx = [ 0,1,0,-1 ]
dy = [ 1,0,-1,0 ]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    union = [(i,j)]
    count = city[i][j]

    while q:
        x,y = q.popleft()

        for d in range(4):
            nx,ny = x + dx[d],y+dy[d]

            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0 and l<=abs(city[nx][ny]-city[x][y])<=r:
                union.append((nx,ny))
                count += city[nx][ny]
                q.append((nx,ny))
                visited[nx][ny] = True

    if len(union) > 1:
        value = count // len(union)
        for x,y in union:
            city[x][y] = value


    return len(union)




cnt = 0
while True:
    flg = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i,j)>1:
                    flg = True
    if not flg:
        break
    # for q in city:
    #     print(q)
    # print('---------')
    cnt +=1
print(cnt)