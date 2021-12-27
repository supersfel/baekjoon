N = int(input())
stair = []
for _ in range(N):
    stair.append(int(input()))
result = []



result.append(stair[0])
result.append(max(stair[0]+stair[1],stair[1]))
result.append(max(stair[0]+stair[2],stair[1]+stair[2]))

for i in range(3,N):
    result.append(max(result[i-2],result[i-3] + stair[i-1])+stair[i])

print(result[-1])
