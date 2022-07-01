import sys
input = sys.stdin.readline

dx = [ 1 , 0 , -1 , 0 ]
dy = [ 0 , -1 , 0 , 1 ]

board = [ [0]*101 for _ in range(101)]

def rotate(nodes,cod,cnt,goal):
    main_x,main_y = cod
    new_nodes = []
    if cnt == goal:
        for i in nodes:
            a,b = i
            board[b][a] = 1
        return nodes

    for node in nodes:
        x,y = node
        x -= main_x
        y -= main_y
        x,y = y*(-1),x
        if [x+main_x,y+main_y] not in nodes:
            new_nodes.append([x+main_x,y+main_y])

    return rotate(nodes + new_nodes,new_nodes[0],cnt+1,goal)


def find_square():
    result = 0
    for i in range(100):
        for j in range(100):
            if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
                result +=1
    return result

n = int(input())
for _ in range(n):
    x,y,d,g = map(int,input().split())
    rotate([[x,y],[x+dx[d],y+dy[d]]],[x+dx[d],y+dy[d]],0,g)

print(find_square())






