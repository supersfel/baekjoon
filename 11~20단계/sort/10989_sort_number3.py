import sys

N = int(sys.stdin.readline())
lst=[0]*10001
for i in range(N):
    n = int(sys.stdin.readline())
    lst[n] +=1

i=0
for j in lst:
    for _ in range(j):
        print(i)
    i+=1