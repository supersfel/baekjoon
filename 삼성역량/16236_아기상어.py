import sys
from collections import deque
input = sys.stdin.readline

dx = [ -1 , 0 , 0 , 1 ]
dy = [ 0 , -1 , 1 , 0 ]

n = int(input())
sea = [ list(map(int,input().split())) for _ in range(n)]
size = 2
cnt = 0
for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
            x,y = i,j

def bfs(x,y):
    global size,cnt
    q = deque([(x,y,0)])
    visit = [ [False]*n for _ in range(n)]
    temp = []
    distance = 1e9
    while q:
        x,y,dist = q.popleft()
        visit[x][y] = True

        for d in range(4):
            nx,ny = x + dx[d], y + dy[d]

            if 0<=nx<n and 0<=ny<n and not visit[nx][ny] and dist < distance:

                if sea[nx][ny] <= size:
                    q.append((nx,ny,dist+1))
                    visit[nx][ny] = True
                    if sea[nx][ny] < size and sea[nx][ny] !=0:
                        temp.append((nx,ny,dist+1))
                        distance = dist+1

    return sorted(temp,key=lambda x: (x[2],x[0],x[1]))

result = 0
while True:
    sea[x][y] = 0
    temp = bfs(x,y)
    if len(temp) ==0:
        break
    x,y,dist = temp[0]

    sea[x][y] = 9
    result += dist
    cnt += 1
    if size == cnt:
        size += 1
        cnt = 0

print(result)