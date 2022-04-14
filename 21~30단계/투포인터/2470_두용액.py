n = int(input())
lst = list(map(int,input().split()))

lst.sort()
start,end = 0,n-1
a,b = lst[start],lst[end]
result = lst[0] + lst[n-1]

while start < end:
    s = lst[start] + lst[end]
    if abs(s) < abs(result):
        a,b = lst[start],lst[end]
        result = s
    if s < 0:
        start +=1
    else :
        end -=1
print(a,b)