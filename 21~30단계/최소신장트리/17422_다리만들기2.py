import sys
input = sys.stdin.readline
n,m = map(int,input().split())
dy = [1,0,-1,0]
dx = [0,1,0,-1]
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
    if a[0] > b[0]:
            parents[a[0]][a[1]] = b
    else:
        parents[b[0]][b[1]] = a

land=[]

for i in range(n):
    for j in range(m):
        if country[i][j]:
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if  0<=nx<n and 0<=ny<m and country[nx][ny]:
                    union([i,j],[nx,ny])
            if parents[i][j] not in land:
                land.append(parents[i][j])

for i in range(len(land)):
    land[i] = find(land[i])
new_land = []
for i in land:
    if i not in new_land:
        new_land.append(i)


dist = []
for i in range(n):
    for j in range(m):
        if not country[i][j]:
            continue
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            cnt = 0
            if 0<= nx < n and 0<= ny < m and parents[i][j]==parents[nx][ny]:
                continue
            while(0<= nx < n and 0<= ny < m):
                if country[nx][ny]:
                    break
                cnt += 1
                nx += dx[k]
                ny += dy[k]
            else:
                continue
            if cnt > 1:
                dist.append([cnt,parents[i][j],parents[nx][ny]])
dist.sort()
result = 0
cnt = 1
for i in dist:
    LEN,A,B = i
    if find(parents[A[0]][A[1]]) != find(parents[B[0]][B[1]]):
        result += LEN
        union(A, B)
        cnt +=1
print(result if cnt==len(new_land) else -1)