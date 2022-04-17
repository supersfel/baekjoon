n = int(input())
lst = [True] * (n+1)

for i in range(2,int((n+1)**0.5)+1):
    if lst[i]:
        for j in range(i*2,n+1,i):
            lst[j] = False
sosu = [0]
for i in range(2,n+1):
    if lst[i]:
        sosu.append(i)

start,end = 0,0
SUM,cnt,LEN = 0,0,len(sosu)

while start < LEN:
    if SUM <= n:
        if SUM ==n:
            cnt +=1
        if end < LEN-1:
            end +=1
            SUM += sosu[end]
        else:
            break
    else:
        SUM -= sosu[start]
        start +=1

print(cnt)