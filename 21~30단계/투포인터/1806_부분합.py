import sys
N,S = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))

start,end = 0,1
result =int(1e9)
SUM,LEN = lst[0],1
while start < N:
    if SUM >= S:
        if LEN < result:
            result = LEN
        SUM -= lst[start]
        LEN -=1
        start +=1
    elif end < N:
        SUM += lst[end]
        LEN +=1
        end += 1
    else:
        start+=1
print(result if result != int(1e9) else 0)