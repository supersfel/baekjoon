from collections import deque
n,k = map(int,input().split())

q = deque([n])
dp = [ 0 for _ in range(100001) ]



while q:
    x = q.popleft()

    if x == k:
        print(dp[x])
        break

    for nx in (x-1,x+1,2*x):
        if 0 <= nx <= 100000 and not dp[nx]:
            if nx == 2*x:
                dp[nx] = dp[x]
            else:
                dp[nx] = dp[x] + 1
            q.append(nx)

