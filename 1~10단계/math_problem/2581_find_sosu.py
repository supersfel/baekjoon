m,n = map(int,input().split())
lst=[]

for i in range(m,n+1):

    f = True
    if i<=1: continue

    for j in range(2,i):
        if i%j==0:
            f=False
            break
    if f:
        lst.append(i)

if len(lst)==0 :
    print(-1)
else :
    print(sum(lst))
    print(min(lst))

