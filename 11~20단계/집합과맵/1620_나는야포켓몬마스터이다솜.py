import sys
input = sys.stdin.readline
n,m = map(int,input().split())
poketmon_num={}
poketmon_alp={}
for i in range(1,n+1):
    poketmon = input().strip()
    poketmon_alp[poketmon] = i
    poketmon_num[i] = poketmon


for _ in range(m):
    order = input().strip()
    if order.isalpha():
        print(poketmon_alp[order])
    else:
        print(poketmon_num[int(order)])
