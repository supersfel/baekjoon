import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n = int(input())
position = []
for i in range(n):
    x,y,z = map(int,input().split())
    position.append((x,y,z,i))

dist = []
for i in range(3):
    position.sort(key=lambda x:x[i])
    for j in range(1,n):
        dist.append((abs(position[j-1][i]-position[j][i]),position[j-1][3],position[j][3]))
dist.sort()

def find(a):
    if a == parents[a]:
        return a
    parents[a] = find(parents[a])
    return parents[a]
def union(a,b):
    a,b = find(a),find(b)
    if a>b:
        parents[a]=b
    else:
        parents[b]=a
result = 0
parents = [ i for i in range(n)]
for cost,a,b in dist:
    if find(a) != find(b):
        union(a,b)
        result +=cost

print(result)