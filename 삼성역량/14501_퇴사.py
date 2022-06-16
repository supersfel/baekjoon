import sys
input = sys.stdin.readline

day , cost = [],[]
n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    day.append(a)
    cost.append(b)

day.reverse()
cost.reverse()

dp = [0]*n
dp[0] = cost[0] if day[0]==1 else 0

for i in range(1,n):

    if i>=day[i]-1:
        dp[i] = max(dp[i-1],dp[i-day[i]]+cost[i])
    else:
        dp[i] = dp[i-1]
print(dp[-1])