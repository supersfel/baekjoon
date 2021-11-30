import sys
# 시간을 최소화 하기위해
T = int(sys.stdin.readline())

for i in range(T):
    a,b = map(int,sys.stdin.readline().split())
    print(a+b)