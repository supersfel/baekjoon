import sys
input = sys.stdin.readline

n,l,r = map(int,input().split())
city = [ list(map(int,input().split())) for _ in range(n)]
dx = [ 0,1 ]
dy = [ 1,0 ]

def find(a,b):
    if parents[a][b] == [a,b]:
        return [a,b]
    na,nb = parents[a][b]
    parents[a][b] = find(na,nb)
    return parents[a][b]

def union(x,y):
    a,b = x
    c,d = y
    a,b = find(a,b)
    c,d = find(c,d)

    if a<=c:
        parents[c][d] = [a,b]
    else:
        parents[a][b] = [c,d]

while True:
    old_city = [ x[:] for x in city]
    parents = [[[i, j] for j in range(n)] for i in range(n)]
    sum_lst = [ x[:] for x in city]
    print(parents)

    for i in range(n):
        for j in range(n):
            for k in range(2):
                ni,nj = i + dx[k], j + dy[k]

                if ni<n and nj<n and l<=abs(city[ni][nj]-city[i][j])<=r:
                    print('-test')
                    union([i,j],[ni,nj])
                    x,y = find(i,j)
                    sum_lst[x][y] += city[ni][nj]

            print(parents)
            for q in sum_lst:
                print(q)
            print('--------')
    break
