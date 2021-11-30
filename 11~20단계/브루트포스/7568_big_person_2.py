N = int(input())
lst=[]
for _ in range(N):
    lst.append(list(map(int,input().split())))

for i in range(N):
    count =1
    for j in range(N):
        if lst[i][0]<lst[j][0] and lst[i][1]<lst[j][1]:
            count +=1
    print(count,end=' ')