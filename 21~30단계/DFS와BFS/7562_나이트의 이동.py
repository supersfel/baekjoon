import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]

for _ in range(t):
    l = int(input())
    sx,sy= map(int,input().split())
    ex,ey = map(int,input().split())
    visited = [ [0 for _ in range(l)]  for __ in range(l)]
    q = deque([[sx,sy]])

    while q:
        x,y = q.popleft()
        if x == ex and y == ey:
            print(visited[x][y])
            break
        for i in range(8):
            nx,ny = x + dx[i],y+ dy[i]
            if 0<= nx < l and 0 <= ny < l and visited[nx][ny] == 0:
                q.append([nx,ny])
                visited[nx][ny] = visited[x][y] +1
