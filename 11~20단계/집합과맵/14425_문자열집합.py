import sys
input = sys.stdin.readline
n,m = map(int,input().split())

S={}
for i in range(n):
   S[input().strip()] = True

cnt=0
for _ in range(m):
    if input().strip() in S:
        cnt +=1
print(cnt)