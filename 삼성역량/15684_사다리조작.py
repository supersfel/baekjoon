import sys
input = sys.stdin.readline

n,m,h = map(int,input().split())

ladder = [ [0] * (n+1) for _ in range(h+1)]
for _ in range(m):
    a,b = map(int,input().split())
    ladder[a][b] = 1


def check_end(start):
    for i in range(1,h+1):
        if ladder[i][start-1] == 1:
            start = start - 1
        elif ladder[i][start] ==1:
            start = start + 1
    return start

def check_game():
    for i in range(1,n):
        if check_end(i) != i:
            break
    else:
        return True
    return False



result = (n-1) * h - m + 1
def dfs(x,y,cnt,flg):
    global result

    # for i in ladder:
    #     print(i)
    # print(x,y,cnt)
    # print(check_game())
    # print('------------')

    if result <= cnt:
        return
    if check_game():
        result = cnt
        return
    else:
        if x == n and y==h-1:
            ladder[x][y]=1
            if check_game():
                result = cnt+1
                return
            ladder[x][y]=0
            return

    if 0<y<n-1:
        ny = y+1
        nx = x
    elif 0<x<h:
        nx = x+1
        ny = 1
    else:
        return

    if ladder[x][y] == 1:
        if ny == 1:
            dfs(nx,ny,cnt,0)
        else:
            dfs(nx,ny,cnt,1)
        return

    if not flg and ladder[x][y+1]==0:
        ladder[x][y] = 1
        dfs(nx,ny,cnt+1,1)
        ladder[x][y] = 0
        dfs(nx,ny,cnt,0)
    else:
        dfs(nx,ny,cnt,0)

dfs(1,1,0,0)



print(-1 if result == (n-1) * h - m + 1 else result)