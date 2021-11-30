import sys
T = int(sys.stdin.readline())

for i in range(T):
    print('%s%s' %(' '*(T-i-1),'*'*(i+1)))