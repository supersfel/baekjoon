T= int(input())
for _ in range(T):
    n = int(input()) + 1
    lst = [True] * n
    sosu_lst = []
    for i in range(2,int(n**0.5)+1):
        if list[i]:
            for j in range(2*i,n,i):
                lst[j] = False
    for i in range(2,n):
        if i > 1 and lst[i] == True :
            sosu_lst.append(i)
    n-=1
    sub = 10000
    for i in sosu_lst:
        if n-i in sosu_lst:

            k = abs(n-i*2)
            if k < sub:
                sub = k
                a,b = i,n-i
    print(a,b)



