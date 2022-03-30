from collections import deque
import copy
m,n = map(int,input().split())
tomato = [ list(map(int,input().split())) for _ in range(n) ]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
cnt = 0

while True:
    for i in tomato:
        if 0 in i:
            break
    else:
        print(cnt)
        break

    old_map = copy.deepcopy(tomato)
    for i in range(n):
        for j in range(m):
            if old_map[i][j] ==1:
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if old_map[nx][ny] == 0:
                            tomato[nx][ny] = 1

    if old_map == tomato:
        print(-1)
        break
    cnt +=1
