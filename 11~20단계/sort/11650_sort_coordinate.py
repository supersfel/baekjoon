import sys
N = int(sys.stdin.readline())
lst=[]
for _ in range(N):
    a,b = map(int,sys.stdin.readline().split())
    lst.append([a,b])

lst.sort()

for i in lst:
    print(i[0],i[1])