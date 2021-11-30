t=int(input())
N=[]
while t!=0:
    N.append(t)
    t=int(input())

for num in N:
    m=num+1
    n=2*num +1
    lst = [True] * (n + 1)
    count = 0

    for i in range(2, int(n ** 0.5) + 1):
        if lst[i]:
            for j in range(2 * i, n, i):
                lst[j] = False

    for i in range(m, n):
        if i > 1 and lst[i] == True:
            count+=1

    print(count)


