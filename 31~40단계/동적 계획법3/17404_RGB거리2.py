import sys
input = sys.stdin.readline

n = int(input())
cost = [ list(map(int,input().split())) for _ in range(n)]
result = []
for i in range(3):
    dp = [ [0,0,0] for _ in range(n) ]
    dp[0] = [1e9,1e9,1e9]
    dp[0][i] = cost[0][i]
    for j in range(1,n):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + cost[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + cost[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + cost[j][2]

    dp[-1][i] = 1e9
    result.append(min(dp[-1]))
print(min(result))
