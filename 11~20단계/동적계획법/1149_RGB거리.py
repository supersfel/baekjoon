import sys

N = int(sys.stdin.readline())
lst = [ list(map(int,sys.stdin.readline().split())) for _ in range(N) ]


for i in range(1, N):
    lst[i][0] += min(lst[i-1][1], lst[i-1][2])
    lst[i][1] += min(lst[i-1][0], lst[i-1][2])
    lst[i][2] += min(lst[i-1][0], lst[i-1][1])
print(min(lst[-1]))