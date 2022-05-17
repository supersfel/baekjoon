import sys
input = sys.stdin.readline

n,m = map(int,input().split())
position = []
for _ in range(n):
    x,y = map(int,input().split())
    position.append((x,y))
path = []
for _ in range(m):
    a,b = map(int,input().split())
    path.append((a,b))
dist = []

for i in range(n):
    for j in range(i,n):
        if i==j:
            continue
        distance = (( position[i][0] - position[j][0] )**2 + (position[i][1] - position[j][1]) **2)**0.5
        dist.append((i+1,j+1,distance))
dist.sort(key=lambda x:x[2])

parents=[i for i in range(n+1)]
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
for a,b in path:
    union(a,b)

for a,b,c in dist:
    if find(a) != find(b):
        union(a,b)
        result += c

print('%.2f'%result)