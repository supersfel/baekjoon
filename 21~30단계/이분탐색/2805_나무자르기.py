import sys
n,m = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))
start,end = 0,1000000000



while start <= end:
    mid = (start+end) //2
    cnt = 0
    for i in lst:
        if i > mid:
            cnt += i-mid

    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)