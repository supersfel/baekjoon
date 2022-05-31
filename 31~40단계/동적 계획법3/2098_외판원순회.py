n = int(input())

INF = int(1e9)
dp = [[INF] * (1 << n) for _ in range(n)]
W = [ list(map(int,input().split())) for _ in range(n)]
def dfs(node,visited):

    if visited == (1<<n)-1:
        if W[node][0]:
            return W[node][0]
        else:
            return INF

    if dp[node][visited] != INF:
        return dp[node][visited]

    for i in range(1,n):
        if not W[node][i]:
            continue
        if visited & (1<<i):
            continue

        dp[node][visited] = min(dp[node][visited],dfs(i,visited | (1<<i)) + W[node][i])
    return dp[node][visited]

print(dfs(0,1))