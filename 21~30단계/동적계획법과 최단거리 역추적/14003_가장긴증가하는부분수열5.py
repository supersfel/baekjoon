from bisect import bisect_left
n = int(input())
lst = [0] + list(map(int,input().split()))
dp = [ 0 ]* (n+1)
tmp = [ -1000000001 ]
cnt = 0

for i in range(1,n+1):
    if tmp[-1] < lst[i]:
        tmp.append(lst[i])
        dp[i] = len(tmp) -1
        cnt = dp[i]
    else:
        dp[i] = bisect_left(tmp,lst[i])
        tmp[dp[i]] = lst[i]
print(cnt)
print(dp)
print(tmp)
result = []
for i in range(n,0,-1):
    if dp[i] == cnt:
        result.append(lst[i])
        cnt -= 1
result.reverse()
print(*result)