import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

n = int(input())
k = int(input())
board = [ [0]*n for _ in range(n) ]

for _ in range(k):
    a,b = map(int,input().split())
    board[a-1][b-1] = -1

l = int(input())
dic = {}
for _ in range(l):
    a,b = map(str,input().split())
    dic[int(a)] = b

board[0][0] = 1
snail = deque([[0,0]])
To = 0


for i in range(1,10000):

    y,x = snail[0]
    nx,ny = x + dx[To], y + dy[To]

    if 0<=nx<n and 0<= ny < n:
        if board[ny][nx] == 1:
            print(i)
            break
        elif board[ny][nx] == -1:
            board[ny][nx] = 1
            snail.appendleft([ny,nx])
        else:
            snail.appendleft([ny,nx])
            board[ny][nx] = 1
            a,b = snail.pop()
            board[a][b] = 0
    else:
        print(i)
        break

    if i in dic:
        if dic[i] =='D':
            To = (To+1)%4
        else:
            To = (To-1)%4



