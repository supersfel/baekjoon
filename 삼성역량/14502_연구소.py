import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())
board = [ list(map(int,input().split())) for _ in range(n) ]

dx = [ 0,1,0,-1 ]
dy = [ 1,0,-1,0 ]


def dfs(x,y):
    if board[x][y] !=2:
        return

    for i in range(4):
        nx,ny = x + dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and not board[nx][ny]:
            board[nx][ny] = 2
            dfs(nx,ny)

def check_dfs():
    for i in range(n):
        for j in range(m):
            dfs(i,j)

    cnt = 0
    for i in board:
        for j in i:
            if j == 0:
                cnt +=1
    return cnt

old_board = [ x[:] for x in  board ]
result = 0
for combi in combinations(range(n*m),3):

    tmp = []
    for i in combi:
        tmp.append([i//m,i%m])


    board = [ x[:] for x in old_board]

    for x,y in tmp:
        if board[x][y] != 0:
            break
        board[x][y] = 1
    else:
        result = max(result,check_dfs())

print(result)