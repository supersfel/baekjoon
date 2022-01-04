N = int(input())
lst = list(map(int,input().split()))
result = [ 0 for _ in range(N) ]

for i in range(N):
    for j in range(i):
        if lst[i] > lst[j] and result[i] < result[j]:
            result[i] = result[j]
    result[i] +=1


print(max(result))
print(result)