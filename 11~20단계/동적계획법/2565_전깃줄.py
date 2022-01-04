n = int(input())
lst = [ list(map(int,input().split())) for _ in range(n) ]
result =[ 0 for _ in range(n)]

lst.sort(key = lambda x:x[0])
lst_b = [ lst[x][1] for x in range(n) ]


for i in range(n):
    for j in range(i):
        if lst_b[i] > lst_b[j] and result[i] < result[j]:
            result[i] = result[j]
    result[i] +=1

print(n - max(result))