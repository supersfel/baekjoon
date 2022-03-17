import sys
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
for _ in range(m):
    s,e = map(int,sys.stdin.readline().split())
    print(s,e)

dp = [ [0 for _ in range(n)] for __ in range(n)]

for i in range(n):
    dp[i][i] = 1

for j in range(n-1):
    if lst[j] == lst[j+1]:
        dp[j][j+1]=1

for i in range(2,n-1):
    for j in range(n-1-i):
        if dp[j][]

for k in dp:
    print(k)


