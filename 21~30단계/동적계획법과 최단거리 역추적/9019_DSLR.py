import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

def bfs(a,b):
    q = deque([a])
    while q:
        num = q.popleft()
        if num == b:
            return
        d1,d2,d3,d4 = num
        D = str(2*int(num) % 10000)
        D = '0'*(4-len(D)) + D

        if int(num) == 0:
            S = '9999'
        else:
            S = str(int(num)-1)
            S = '0'*(4-len(S)) + S

        L = d2+d3+d4+d1
        R = d4+d1+d2+d3

        for i,j in ((D,'D'),(S,'S'),(L,'L'),(R,'R')):
            int_i = int(i)
            if dp[int_i] == '':
                dp[int_i] = num+j
                q.append(i)

for _ in range(T):
    a,b = map(str,input().split())
    a = '0' * (4 - len(a)) + a
    b = '0' * (4 - len(b)) + b
    dp = [ '' for __ in range(10000)]
    bfs(a,b)
    result = [dp[int(b)][4]]
    tmp = dp[int(b)][0:4]
    while tmp != a:
        result.append(dp[int(tmp)][4])
        tmp = dp[int(tmp)][0:4]
    result.reverse()
    print(*result,sep='')


