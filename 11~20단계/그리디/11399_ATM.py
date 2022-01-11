n = int(input())
lst =  [0] + list(map(int, input().split()))
result = [0]
lst.sort()
for i in range(1,n+1):
    result.append(result[i-1] + lst[i])

print(sum(result))
