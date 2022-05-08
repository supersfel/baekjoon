import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
n,m = map(int,input().split())

parents = [i for i in range(n+1)]
def union(a,b):
    a,b = find(a),find(b)

    if a <= b:
        parents[b] = a
    else:
        parents[a] = b

def find(a):
    if parents[a] ==a:
        return a
    parents[a] = find(parents[a])
    return parents[a]



for _ in range(m):
    order , a , b = map(int,input().split())

    if order:
        print('YES' if find(a)==find(b) else 'NO')
    else:
        union(a, b)