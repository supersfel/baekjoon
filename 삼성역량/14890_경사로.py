import sys
input = sys.stdin.readline

n,l = map(int,input().split())

board = [ list(map(int,input().split())) for _ in range(n)]

def check():
    global cnt
    for i in range(n):
        idx = 0
        visited = [0] * n
        flg = 1
        while idx<(n-1) and flg:
            num = board[i][idx]
            nnum = board[i][idx+1]
            if abs(num - nnum)>1:
                flg = 0
            elif num > nnum:
                for j in range(1,l+1):
                    if idx+j < n and not visited[idx+j] and board[i][idx+j] == nnum:
                        visited[idx+j]=1
                    else:
                        flg=0
                        break
                else:
                    idx += l - 1
            elif num < nnum:
                for j in range(l):
                    if idx-j >= 0 and not visited[idx-j] and board[i][idx-j] == num:
                        visited[idx-j]=1
                    else:
                        flg = 0
            idx += 1
        if flg:
            cnt +=1
cnt = 0
check()
board = [ [board[j][i] for j in range(n)] for i in range(n)]
check()
print(cnt)
