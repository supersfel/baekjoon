n,k = map(int,input().split())
lst=[1,1]
for a in range(2,1001):
    lst.append(lst[-1]*a)

print( (lst[n] // ( lst[k] * (lst[n-k]) )) % 10007 )