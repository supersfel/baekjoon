from collections import deque
n,m = map(int,input().split())


q = deque([n])
dp= [ 0 for _ in range(100001)]

while q:
    x = q.popleft()
    if x == m :
        print(dp[x])
        break

    for nx in (x-1,x+1,2*x):
        if 0 <= nx <= 100000 and not dp[nx]:
            dp[nx] = dp[x] +1
            q.append(nx)


