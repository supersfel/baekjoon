import sys
input = sys.stdin.readline

n,m = map(int,input().split())
parents = [ i for i in range(n)]

def find(a):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a])
    return parents[a]
def union(a,b):
    a,b = find(a),find(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a

result = 0
for i in range(1,m+1):
    a,b = map(int,input().split())
    if find(a) == find(b) and result == 0 :
        result = i
    union(a,b)

print(result)
