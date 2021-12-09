N,M = map(int,input().split())

lst=[1] * M
index = -1
flag = 0

while( lst[0] <= N ):
    if len(set(lst)) == len(lst):
        print(' '.join(map(str,lst)))

    while ( lst[index] == N and index != -M ):
        lst[index]=1
        index -= 1
        flag = 1

    lst[index] += 1

    if flag:
        index = -1
        flag = 0