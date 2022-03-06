import sys
n,c = map(int,sys.stdin.readline().split())
lst = [ int(sys.stdin.readline()) for _ in range(n) ]

lst.sort()
start,end = 0,100000000

while start <= end:
    mid = (start + end) //2
    cnt = 1
    tmp = [lst[0]]
    for i in lst:
        if i-tmp[-1] > mid:
            cnt +=1
            tmp.append(i)
    if cnt >= c:
        start = mid +1
    else :
        end = mid -1
print(max(start,end))