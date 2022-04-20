n = int(input())
lst = list(map(int,input().split()))
dp = [[lst[i]] for i in range(n)]
for i in range(1,n):
    for j in range(i-1,-1,-1):
        if lst[i] > lst[j] and len(dp[j]) >= len(dp[i]):
            dp[i] = dp[j] + [ lst[i] ]

result = max(dp,key=len)
print(len(result))
for i in result:
    print(i,end=' ')