import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

def bfs(a,b):
    q = deque([(a,'')])
    while q:
        num,result = q.popleft()

        if num == b:
            print(result)
            return

        D = (2*num)%10000
        if not dp[D]:
            q.append((D,result+'D'))
            dp[D] = True
        S = (num-1)%10000
        if not dp[S]:
            q.append((S,result+'S'))
            dp[S] = True
        L = (10 * num + (num // 1000)) % 10000
        if not dp[L]:
            q.append((L, result + "L"))
            dp[L] = True

        # 4
        R = (num // 10 + (num % 10) * 1000) % 10000
        if not dp[R]:
            q.append((R, result + "R"))
            dp[R] = True

for _ in range(T):
    a,b = map(int,input().split())
    dp = [False] * 10000
    bfs(a,b)


