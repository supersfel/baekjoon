n = int(input())
lst = list(map(int,input().split()))

start,end = 1,n
dp = [0]

for i in range(n):
    start,end = 0,len(dp)-1

    while start<=end:
        mid = (start + end) //2
        # print('start',start,'end',end,'mid : ',mid)
        if dp[mid] <lst[i]:
            start = mid + 1
        else:
            end = mid -1
    if start >= len(dp):
        dp.append(lst[i])
    else:
        dp[start] = lst[i]
    # print(dp)

print(len(dp)-1)