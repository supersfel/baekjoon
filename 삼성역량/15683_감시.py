import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = [ list(map(int,input().split())) for _ in range(n)]

cctv_info = [0]*6
cctv_info[1] = [ [[0,1]], [[1,0]] , [[0,-1]] , [[-1,0]] ]
cctv_info[2] = [ [[0,1],[0,-1]] , [[1,0],[-1,0]] ]
cctv_info[3] = [ [[-1,0],[0,1]],[[0,1],[1,0]],[[1,0],[0,-1]] ,[[0,-1],[-1,0]]]
cctv_info[4] = [ [[0,-1],[-1,0],[0,1]] ,[[-1,0],[0,1],[1,0]],[[0,1],[1,0],[0,-1]],[[1,0],[0,-1],[-1,0]] ]
cctv_info[5] = [ [[0,1],[1,0],[0,-1],[-1,0]] ]

cctvs = []
for i in range(n):
    for j in range(m):
        if board[i][j] != 0 and board[i][j] != 6:
            cctvs.append([board[i][j],i,j])
len_cctv = len(cctvs)

def check_size():
    cnt = 0
    for i in board:
        for j in i:
            if j == 0:
                cnt +=1
    return cnt

result = 10e9

def dfs(cctv,odr):
    global board,result
    num,x,y = cctv

    for direct in cctv_info[num]:
        old_board = [x[:] for x in board]
        for dx,dy in direct:
            nx,ny = x + dx,y + dy


            while 0<= nx < n and 0<= ny < m and board[nx][ny] != 6:
                if not board[nx][ny]:
                    board[nx][ny] = '#'

                nx,ny = nx + dx,ny + dy

        nx_odr = odr + 1
        if nx_odr == len_cctv:
            result = min(result,check_size())
        elif nx_odr < len_cctv:
            dfs(cctvs[nx_odr],nx_odr)

        board = [x[:] for x in old_board]

if len_cctv==0:
    print(check_size())
else:
    dfs(cctvs[0],0)
    print(result)