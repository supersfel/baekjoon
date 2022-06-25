import sys
from collections import deque
input = sys.stdin.readline

n,m,x,y,k = map(int,input().split())
board = [ list(map(int,input().split())) for _ in range(n)]
orders = list(map(int,input().split()))

dice_c = deque([0,0,0,0])
dice_r = deque([0,0,0])

dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

def move(di):
    if di == 1:
        dice_r.append(dice_r.popleft())
        dice_c[3],dice_r[2] = dice_r[2],dice_c[3]
        dice_c[1] = dice_r[1]
    elif di == 2:
        dice_r.appendleft(dice_r.pop())
        dice_c[3], dice_r[0] = dice_r[0], dice_c[3]
        dice_c[1] = dice_r[1]
    elif di == 3:
        dice_c.appendleft(dice_c.pop())
        dice_r[1] = dice_c[1]
    elif di ==4:
        dice_c.append(dice_c.popleft())
        dice_r[1] = dice_c[1]



for order in orders:
    nx,ny = x + dx[order] , y + dy[order]

    if 0<=nx<n and 0<=ny<m:
        move(order)
        if board[nx][ny]:
            dice_r[1] = board[nx][ny]
            dice_c[1] = board[nx][ny]
            board[nx][ny]=0
        else:
            board[nx][ny] = dice_r[1]
        x,y = nx,ny

        print(dice_c[3])




