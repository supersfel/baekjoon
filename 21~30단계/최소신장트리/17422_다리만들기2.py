import sys
input = sys.stdin.readline
n,m = map(int,input().split())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
country = []
for _ in range(n):
    country.append(list(map(int,input().split())))

parents = []
for i in range(n):
    tmp = []
    for j in range(m):
        tmp.append([i,j])
    parents.append(tmp)

def find(a):
    i,j = a
    if parents[i][j] == a:
        return a
    parents[i][j] = find(parents[i][j])
    return parents[i][j]
def union(a,b):
    a,b = find(a),find(b)
    if a == b:
        return
    if a[0] < b[0]:
        parents[a[0]][a[1]] = b
    else:
        parents[b[0]][b[1]] = a

for i in range(n):
    for j in range(m):
        if country[i][j]:
            for i in range(4):
                nx = i + dx[i]
                ny = i + dy[i]
                if country[nx][ny]:
                    union([i,j],[nx,ny])

for i in parents:
    print(i)

