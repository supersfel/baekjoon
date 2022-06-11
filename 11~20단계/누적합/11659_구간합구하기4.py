import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = list(map(int,input().split()))
S =[0,lst[0]]
for i in range(1,n):
    S.append(S[-1]+lst[i])

for _ in range(m):
    a,b = map(int,input().split())
    print(S[b]-S[a-1])