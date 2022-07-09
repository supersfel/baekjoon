import sys
input = sys.stdin.readline
from collections import deque


n,m,k = map(int,input().split())
A = [ list(map(int,input().split())) for _ in range(n)]
trees = [ [ deque() for _ in range(n)] for _ in range(n)]
ground = [ [5] * (n) for _ in range(n)]
dead_trees = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x,y,z = map(int,input().split())
    trees[x-1][y-1].append(z)

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]



for o in range(k):
#봄,여름
    for i in range(n):
        for j in range(n):
            for q in range(len(trees[i][j])):
                if trees[i][j][q] > ground[i][j]:
                    for _ in range(q,len(trees[i][j])):
                        dead_trees[i][j].append(trees[i][j].pop())
                    break
                ground[i][j] -= trees[i][j][q]
                trees[i][j][q] += 1

    for i in range(n):
        for j in range(n):
            while dead_trees[i][j]:
                ground[i][j] += dead_trees[i][j].pop() //2


    #가을
    for i in range(n):
        for j in range(n):
            for q in range(len(trees[i][j])):
                if trees[i][j][q]%5 ==0:
                    for d in range(8):
                        ni,nj = i +dx[d],j+dy[d]
                        if 0<=ni<n and 0<=nj<n:
                            trees[ni][nj].insert(0,1)
            ground[i][j] += A[i][j]
    #겨울




    cnt = 0
    print(f'============={o+1}년=============')
    for i in trees:
        print(i)
    print('--------------------------')
    for i in ground:
        print(i)
    for i in trees:
        for j in i:
            cnt += len(j)
    print('cnt : ', cnt)

cnt = 0
for i in trees:
    for j in i:
        cnt += len(j)

print(cnt)