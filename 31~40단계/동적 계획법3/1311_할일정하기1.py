def bit_count(x):
    cnt = 0
    while x:
        cnt += x & 1
        x >>= 1
    return cnt

n = int(input())
D = [ list(map(int,input().split())) for _ in range(n)]

dp = [1e9] * (1<<n)
dp[0] = 0

for i in range(1<<(n)):
    k = bit_count(i)
    for j in range(n):
        if not i & (1<<j):
            dp[i|1<<j] = min ( dp[i|1<<j] , dp[i] + D[k][j])

print(dp[-1])