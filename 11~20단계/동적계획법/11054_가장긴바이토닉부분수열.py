N = int(input())
lst = list(map(int,input().split()))

increase = [ 0 for _ in range(N)]
decrease = [ 0 for _ in range(N)]
result = [ 0 for _ in range(N) ]

for i in range(N):
    for j in range(i):
        if lst[i] > lst[j] and increase[i] < increase[j]:
            increase[i] = increase[j]
    increase[i] +=1

for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if lst[i] > lst[j] and decrease[i] < decrease[j]:
            decrease[i] = decrease[j]
    decrease[i] +=1

for i in range(N):
    result[i] = increase[i]+decrease[i] - 1

print(max(result))