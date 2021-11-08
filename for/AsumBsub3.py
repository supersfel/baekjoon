"""
T = int(input())
c=[]
for t in range(T):
    a,b = map(int,input().split())
    c.append(a+b)

for t in range(T):
    print(c[t])
"""

import sys
# 시간을 최소화 하기위해
t = int(sys.stdin.readline())
for i in range(t) :
    readList = sys.stdin.readline()
    a,b = list(map(int,readList.split()))
    print(a+b)