i,j = map(int,input().split())
map = [ list(map(int,input().split())) for _ in range(i) ]

# print(map)
visited = [ [ -1 for _ in range(j)] for __ in range(i)]
# print(visited)
dx = [1,0,-1,0]
dy = [0,1,0,-1]


def f(x,y):
    # for k in visited:
    #     print(k)
    # print('-------------------')
    if x == i-1 and y == j-1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0

    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]

        if 0<= nx < i and 0 <= ny < j:
            if map[nx][ny] < map[x][y]:
                visited[x][y] += f(nx,ny)

    # print('visited[',x,'][',y,']',visited[x][y])
    # for k in visited:
    #     print(k)
    # print('-------------------')
    return visited[x][y]



print(f(0,0))

