import sys
from itertools import combinations
n,c = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))
a,b = lst[:n//2] , lst[n//2:]
A,B = [],[]
cnt = 1
for i in range(1,len(a)+1):
    for j in combinations(a,i):
        SUM = sum(j)
        if SUM <= c:
            A.append(SUM)
for i in range(1,len(b)+1):
    for j in combinations(b, i):
        SUM = sum(j)
        if SUM <= c:
            B.append(SUM)
B.sort()

for i in A:
    start,end = 0 , len(B)
    while start < end:
        mid = (start+end)//2
        if i + B[mid] <= c:
            start = mid+1
        else:
            end = mid   #이분탐색 +1은 start에
    cnt += end   #end값을 더해야함 mid값 x
print(len(A) + len (B) + cnt)
#냅색