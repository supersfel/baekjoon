import sys
input = sys.stdin.readline

n,m = map(int,input().split())
r,c,d = map(int,input().split())
board = [ list(map(int,input().split())) for _ in range(n) ]

dx = [ -1,0,1,0 ]
dy = [ 0,1,0,-1 ]

cnt = 0
def dfs(x,y,d):
    global cnt
    if not board[x][y]:
        board[x][y] =2
        cnt +=1

    for i in range(4):
        d = (d-1) % 4
        nx,ny = x + dx[d], y + dy[d]

        if 0<=nx<n and 0<=ny<m and not board[nx][ny]:
            dfs(nx,ny,d)
            break
    else:
        d = (d-2)%4
        nx,ny = x + dx[d],y+dy[d]
        if board[nx][ny] ==1:
            return
        else:
            dfs(nx,ny,(d-2)%4)

dfs(r,c,d)
print(cnt)