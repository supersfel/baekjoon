from collections import deque
import copy
m,n = map(int,input().split())
tomato = [ list(map(int,input().split())) for _ in range(n) ]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
cnt = 1

while True:
    flag = True
    z_flag = False

    for i in range(n):
        for j in range(m):
            if tomato[i][j]==0:
                z_flag = True
            elif tomato[i][j] == cnt:
                for k in range(4):
                    nx,ny = i+dx[k],j+dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if tomato[nx][ny] == 0:
                            tomato[nx][ny] = cnt+1
                            flag=False
    if flag:
        if z_flag:
            print(-1)
            break
        else:
            print(cnt-1)
            break
    cnt+=1



