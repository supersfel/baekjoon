from bisect import bisect_left

n = input()
lst = list(map(int,input().split()))
dp = []

for i in lst:
    k = bisect_left(dp,i)
    if k > len(dp):
        dp.append(i)
    else:
        dp[k] = i

print(len(dp))