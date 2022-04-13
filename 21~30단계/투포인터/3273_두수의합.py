n = int(input())
lst = list(map(int,input().split()))
lst.sort()
x = int(input())

start,end,cnt =0,n-1,0

while start < end:
    s = lst[start] + lst[end]
    if s < x:
        start +=1
    elif s > x:
        end -= 1
    else:
        cnt +=1
        start +=1
print(cnt)