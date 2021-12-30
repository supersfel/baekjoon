N = int(input())
lst = [0]

for _ in range(N):
    lst.append(int(input()))


result = [0]
result.append(lst[1])
if N>1:
    result.append(lst[1] + lst[2])

for i in range(3,N+1):
    result.append(max( result[i-2] + lst[i], result[i-3]+lst[i-1]+ lst[i], result[i-1] ) )

print(result[N])