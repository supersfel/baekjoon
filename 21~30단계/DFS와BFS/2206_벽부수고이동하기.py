from collections import deque
n,m = map(int,input().split())
graph = [ list(map(int,input())) for _ in range(n) ]
visited = [[[0,0] for _ in range(m)] for __ in range(n)]
dx = [ 0,1,0,-1 ]
dy = [ 1,0,-1,0 ]


def bfs():
    q = deque()
    q.append([0,0,0])
    visited[0][0][0] = 1

    while q:
        x,y,f = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][f]

        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny][f] == 0:
                    q.append([nx,ny,f])
                    visited[nx][ny][f] = visited[x][y][f] + 1
                if graph[nx][ny] == 1 and f ==0:
                    q.append([nx,ny,f+1])
                    visited[nx][ny][f+1] = visited[x][y][f] +1

    return -1

print(bfs())

