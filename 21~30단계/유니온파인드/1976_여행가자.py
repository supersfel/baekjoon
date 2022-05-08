import sys
input = sys.stdin.readline
n=int(input())
m=int(input())

def find(a):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a])
    return parents[a]

def union(a,b):
    a,b = find(a),find(b)
    if a<b:
        parents[b] = a
    else:
        parents[a] = b

parents = [ i for i in range(n+1)]
for i in range(1,n+1):
    lst = [0] + list(map(int,input().split()))
    for j in range(i,n+1):
        if lst[j]==1:
            union(i,j)

plan = list(map(int,input().split()))
tmp = find(plan[0])
for i in plan:
    if find(i) != tmp:
        print('NO')
        break
else:
    print('YES')
