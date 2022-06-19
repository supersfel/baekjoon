from collections import deque

n = int(input())
board = [ list(map(int,input().split())) for _ in range(n)]
q = deque([])

dx = [ 1,0,-1,0 ]
dy = [ 0,1,0,-1 ]

def get(i,j):
    if board[i][j]:
        q.append(board[i][j])
        board[i][j]=0

def merge(i,j,k):
    while q:
        tmp = q.popleft()
        if not board[i][j]:
            board[i][j] = tmp
        elif board[i][j] == tmp:
            board[i][j] = tmp*2
            i,j = i - dy[k],j-dx[k]
        else:
            i, j = i - dy[k], j - dx[k]
            board[i][j] = tmp

def do(k,cnt):
    global result
    if k==0:
        for i in range(n):
            for j in range(n-1,-1,-1):
                get(i,j)
            merge(i,n-1,k)
    elif k==1:
        for j in range(n):
            for i in range(n-1,-1,-1):
                get(i,j)
            merge(n-1,j,k)
    elif k==2:
        for i in range(n):
            for j in range(n):
                get(i,j)
            merge(i,0,k)
    elif k==3:
        for j in range(n):
            for i in range(n):
                get(i,j)
            merge(0,j,k)

    # print(f'방향 : {k},cnt : {cnt}')
    for i in board:
        result = max(result,max(i))
    #     print(i)
    # print(result)
    # print('---------------')

result = 0
def f(cnt):
    global board
    if cnt >= 5:
        return
    tmp_board = [ x[:] for x in board]

    for k in range(4):
        board = [ x[:] for x in tmp_board]
        # for i in board:
        #     print(i)
        # print('to')
        do(k,cnt)
        f(cnt+1)

f(0)
print(result)