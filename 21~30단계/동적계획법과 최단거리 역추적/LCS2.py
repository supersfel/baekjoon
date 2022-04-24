import sys
input = sys.stdin.readline
a = input().strip()
b = input().strip()

dp = [ [0 for _ in range(len(b)+1)] for __ in range(len(a)+1)]
result= [ ['' for _ in range(len(b)+1)]  for __ in range(len(a)+1)]
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1]==b[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
            result[i][j] = result[i-1][j-1] + a[i-1]
        else:
            if dp[i][j-1] > dp[i-1][j]:
                result[i][j] = result[i][j-1]
                dp[i][j] = dp[i][j-1]
            else:
                result[i][j] = result[i-1][j]
                dp[i][j] = dp[i-1][j ]
print(dp[-1][-1])
print(result[-1][-1])