import sys
n,k = map(int, sys.stdin.readline().split())

item = [[0,0]]
for i in range(1,n+1):
    item.append(list(map(int,sys.stdin.readline().split())))
result = [ [0]  * (k + 1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= item[i][0]:
            result[i][j] = max(result[i-1][j],result[i-1][j-item[i][0]] + item[i][1])
        else :
            result[i][j] = result[i-1][j]

print(result[-1][-1])

print(item)
for i in result:
    print(i)