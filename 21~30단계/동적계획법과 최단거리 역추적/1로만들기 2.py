n = int(input())
dp = [ [] for i in range(n+1) ]
dp[1].append(1)

for i in range(1,n+1):

    LEN = len(dp[i])
    if i*3 <= n:
        if len(dp[i*3]) == 0 or LEN <len(dp[i*3]) :
            dp[i*3] =  [i*3] +dp[i]
    if i*2 <= n:
        if len(dp[i*2]) == 0 or LEN <len(dp[i*2]) :
            dp[i*2] = [i*2] +  dp[i]
    if i+1 <= n:
        if len(dp[i+1]) == 0 or LEN <len(dp[i+1]) :
            dp[i+1] = [i+1] + dp[i]

print(len(dp[n])-1)
for i in dp[n]:
    print(i,end=' ')
