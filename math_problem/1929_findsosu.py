m,n = map(int,input().split())
lst = [True]*(n+1)
n+=1

for i in range(2,int(n**0.5)+1):
    if lst[i]:
        for j in range(2*i,n,i):
            lst[j] = False


for i in range(m,n):
    if i>1 and lst[i] == True:
        print(i)
