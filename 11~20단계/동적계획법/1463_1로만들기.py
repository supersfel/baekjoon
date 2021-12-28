N = int(input())
lst = [0] * (N+1)

for i in range(2,N+1):
    lst[i] = lst[i-1] + 1
    if i%3 ==0:
        lst[i] = min(lst[i],lst[i//3]+1)
    if i%2 ==0:
        lst[i] = min(lst[i],lst[i//2]+1)


print(lst[-1])