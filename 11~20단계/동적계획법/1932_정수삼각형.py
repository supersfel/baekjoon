n = int(input())
lst = [ list(map(int,input().split())) for _ in range(n)]

for line in range(1,n):
    lst[line][0] += lst[line - 1][0]
    lst[line][-1] += lst[line-1][-1]
    for num in range(1,line):
        lst[line][num] += max(lst[line-1][num],lst[line-1][num-1])
print(max(lst[-1]))