import sys
n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    lst.append(list(map(int,sys.stdin.readline().split())))

lst.sort()
lst.sort(key = lambda x : x[1])
count,num = 0,0

for start,end in lst:
    if start >= num :
        count +=1
        num = end

print(count)