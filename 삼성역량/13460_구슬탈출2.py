import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

dx = [ 1,0,-1,0 ]
dy = [ 0,1,0,-1 ]

board = []
for _ in range(n):
    board.append(input())

R_co,O_co,B_co = [],[],[]
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            R_co = [i,j]
        elif board[i][j] == 'B':
            B_co = [i,j]
        elif board[i][j] == 'O':
            O_co = [i,j]

q = deque([ [R_co,B_co,0] ])

while q:
    R,B,cnt = q.popleft()

    if cnt > 10:
        print(-1)
        break
    if B == O_co:
        continue
    elif R == O_co:
        print(cnt)
        break

    for i in range(4):
        # print(R, B)
        Rnx,Rny = R[1],R[0]
        while True:
            if board[Rny + dy[i]][Rnx + dx[i]] == '#':
                break
            Rnx,Rny = Rnx + dx[i],Rny + dy[i]
            if board[Rny][Rnx] =='O':
                break


        Bnx, Bny = B[1], B[0]
        while True:
            if board[Bny + dy[i]][Bnx + dx[i]] == '#':
                break
            Bnx, Bny = Bnx + dx[i], Bny + dy[i]
            if board[Bny][Bnx] =='O':
                break

        if Rnx == Bnx and Rny == Bny and board[Bny][Bnx] != 'O':
            if dx[i] == 0:
                if B[0] * dy[i] < R[0] * dy[i]:
                    Bny = Bny - dy[i]
                else:
                    Rny = Rny - dy[i]
            else:
                if B[1] * dx[i] < R[1] * dx[i]:
                    Bnx = Bnx - dx[i]
                else:
                    Rnx = Rnx - dx[i]

        for r,b,c in q:
            if r == [Rny,Rnx] and b == [Bny,Bnx]:
                break
        else:
            q.append([[Rny,Rnx],[Bny,Bnx],cnt+1])


